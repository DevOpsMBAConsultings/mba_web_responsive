# mba-oca-web-responsive

Vendored del módulo OCA `web_responsive` (theme responsive para el backend de Odoo 20).

## Por qué existe este repo

El branch `20.0` de [`OCA/web`](https://github.com/OCA/web) todavía no trae los
módulos (solo scaffolding). Como se necesita `web_responsive` en Odoo 20, se
versionó una copia del módulo ya portado a 20.0.

## Estado

- Versión `20.0.1.0.0` (ya lista para Odoo 20, sin migración pendiente).
- Módulo single: el repo es el módulo (`__manifest__.py` en la raíz).
- Se conservan `author`, `maintainers` y `license` (`LGPL-3`) originales de OCA.

Cuando OCA publique el port oficial de `web_responsive` para 20.0, evaluar
reemplazar este repo por el upstream.
