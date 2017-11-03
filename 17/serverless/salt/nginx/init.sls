nginx:
  pkg.installed:
  service.running:
    - require:
      - pkg: nginx

/usr/share/nginx/html/:
  file.recurse:
    - source: salt://web
    - template: jinja
    - require:
      - pkg: nginx
    - watch_in:
      - service: nginx