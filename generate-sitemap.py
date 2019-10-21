from tutorial import run


def generate_sitemap():
    sitemap = ''
    for o in run.chapters.values():
        sitemap += (
            '<url>\n' +
            '    <loc>https://dash.plot.ly{}</loc>\n'.format(o['url']) +
            '</url>\n'
        )
    with open('tutorial/static/sitemap.xml', 'w') as f:
        f.write(
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n' +
            '<!-- autogenerated by generate-sitemap.py - do not modify manually -->' +
            sitemap +
            '</urlset>'
        )


if __name__ == '__main__':
    generate_sitemap()