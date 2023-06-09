from collections import defaultdict

from docutils import nodes
from sphinx.util.docutils import SphinxDirective


class LabelRequestNode(nodes.General, nodes.Element):
    def __init__(self, requested_labels, *args, **kwargs):
        super().__init__(requested_labels, *args, **kwargs)
        self._requested_labels = requested_labels

    @classmethod
    def from_raw_content(cls, raw_content):
        requested_labels = [
            label.strip()
            for label in '\n'.join(raw_content).split(',')
        ]
        return cls(requested_labels)

    @property
    def requested_labels(self):
        return self._requested_labels


class LabelRequestDirective(SphinxDirective):
    has_content = True

    def run(self):
        label_request_node = LabelRequestNode.from_raw_content(self.content)
        self.state.nested_parse(self.content, self.content_offset, label_request_node)
        return [label_request_node]


def build_label_to_document_mapping(app, env):
    label_document_pairs = {
        (label.strip(), doc_name)
        for doc_name, doc_meta in env.metadata.items()
        for label in doc_meta.get('labels', '').split(',')
    }
    label_to_document_mapping = defaultdict(set)
    for label, doc_name in label_document_pairs:
        label_to_document_mapping[label].add(doc_name)

    env.label_to_document_mapping = label_to_document_mapping


def replace_label_request_nodes_with_doc_refs(app, doctree, docname):
    all_label_request_nodes = doctree.findall(LabelRequestNode)
    label_to_document_mapping = app.env.label_to_document_mapping

    for label_request_node in all_label_request_nodes:
        requested_labels = label_request_node.requested_labels
        labeled_doc_names = set()

        for requested_label in requested_labels:
            try:
                doc_names = label_to_document_mapping[requested_label]
            except KeyError:
                continue

            labeled_doc_names |= doc_names

        documents_list_text = ', '.join(labeled_doc_names or 'NO DOCUMENTS FOUND')
        replacement_document_list_nodes = [nodes.Text(
            f'The requested labels ({", ".join(requested_labels)}) are present '
            f'in the following documents: {documents_list_text}.',
        )]
        label_request_node.replace_self(replacement_document_list_nodes)


def setup(app):
    app.add_node(LabelRequestNode)
    app.add_directive('request-labels', LabelRequestDirective)

    app.connect('env-updated', build_label_to_document_mapping)

    app.connect('doctree-resolved', replace_label_request_nodes_with_doc_refs)

    return {
        'version': 'builtin',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
