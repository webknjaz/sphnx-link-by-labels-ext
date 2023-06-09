[![SWUbanner]][SWUdocs]


# In-tree Sphinx example, with a directive linking docs having certain labels


## How to build this

1. Install the deps

   ```console
   pip install -r requirements.in -c requirements.txt
   ```

2. Run the build
   ```console
   sphinx-build -b html -j auto -d ./build/doctrees -T -n -W --keep-going -E ./source/ ./build/
   ```

3. Open it
   ```console
   xdg-open "$(pwd)"/build/index.html
   ```


[SWUbanner]:
https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner-direct-single.svg
[SWUdocs]:
https://github.com/vshymanskyy/StandWithUkraine/blob/main/docs/README.md
