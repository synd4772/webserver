from http.server import HTTPServer, BaseHTTPRequestHandler
import html_handler
import templater

count = 0


def shop_page(x, _path, default_html_page: html_handler.HTMLElementsHandler):
    html_code = default_html_page.get_html_code()
    code = templater.Template(html_code)
    code = code.render(path2="", path=_path[1:])
    default_html_page.set_html_code(code)
    default_html_page.push_into_element(element_id="num2", code_fragment='<h1>SHOP</h1>')

    x.wfile.write(default_html_page.get_html_code().encode())


def test(x, _path, default_html_page):
    html_code = default_html_page.get_html_code()
    code = templater.Template(html_code)
    code = code.render(path2="", path=_path[1:])
    default_html_page.set_html_code(code)

    x.wfile.write(default_html_page.get_html_code().encode())


def not_find(x, default_html_page):
    html_code = default_html_page.get_html_code()
    code = templater.Template(html_code)
    code = code.render(path2="index", path='home')
    default_html_page.set_html_code(code)

    x.wfile.write(default_html_page.get_html_code().encode())


html_web_pages = {"shop": shop_page, "test": test}


class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global count
        page = False
        count += 1
        print(count)
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        default_html_page = html_handler.HTMLElementsHandler('index.html')

        for key, value in html_wep_pages.items():
            if key == self.path[1:]:

                page = True
                value(self, self.path, default_html_page)
        if not page:
            not_find(self, default_html_page)


def main():
    PORT = 8000
    server = HTTPServer(('', PORT), helloHandler)
    print(f"Server running on port {PORT}")
    server.serve_forever()


if __name__ == "__main__":
    main()
