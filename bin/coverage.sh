py.test --cov-config .coveragerc \
        --cov-report html \
        --cov tests \
        --cov bookshelf \
        --cov bookmarks \
        --cov account \
        --cov auth \
        --cov tags && \
python -c "import webbrowser, os; \
           webbrowser.open('file://' + os.getcwd() + \
                           '/.coverage_html/index.html')"
