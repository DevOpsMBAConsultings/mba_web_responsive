# mba_web_responsive

Theme responsive para el backend de Odoo 20, basado en el módulo OCA
`web_responsive` (vendored y renombrado).

## Por qué existe este repo

El branch `20.0` de [`OCA/web`](https://github.com/OCA/web) todavía no trae los
módulos (solo scaffolding). Se vendoreó una copia del módulo ya portado a 20.0 y
se renombró el nombre técnico a `mba_web_responsive` (módulo individual, `_`),
siguiendo la convención: dash (`-`) para repos con módulos, underscore (`_`)
para un módulo.

## Estado

- Versión `20.0.1.0.0`.
- Módulo single: el repo es el módulo (`__manifest__.py` en la raíz).
- Nombre técnico del módulo: `mba_web_responsive`.
- Se conservan `author` y `license` (`LGPL-3`) originales de OCA.

## Despliegue

```bash
git clone git@github.com:DevOpsMBAConsultings/mba_web_responsive.git mba_web_responsive
```
