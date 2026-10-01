# Copyright 2016-2017 LasLabs Inc.
# Copyright 2017-2018 Tecnativa - Jairo Llopis
# Copyright 2018-2019 Tecnativa - Alexandre Díaz
# Copyright 2021 ITerra - Sergey Shebanin
# Copyright 2023 Onestein - Anjeel Haria
# Copyright 2023 Taras Shabaranskyi
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Web Responsive",
    "summary": "Responsive web client, community-supported",
    "version": "20.0.1.0.0",
    "category": "Website",
    "website": "https://github.com/OCA/web",
    "author": "LasLabs, Tecnativa, ITerra, Onestein, Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "installable": True,
    "depends": ["web", "web_tour", "mail"],
    "development_status": "Production/Stable",
    "maintainers": ["Tardo", "SplashS"],
    "excludes": ["web_enterprise"],
    "data": [
        "views/res_users_views.xml",
    ],
    "assets": {
        "web._assets_primary_variables": {
            "/mba_web_responsive/static/src/legacy/scss/form_variable.scss",
            "/mba_web_responsive/static/src/legacy/scss/primary_variable.scss",
        },
        "web.assets_backend": [
            "mba_web_responsive/static/src/lib/fuse/fuse.basic.min.js",
            "/mba_web_responsive/static/src/legacy/scss/mba_web_responsive.scss",
            "/mba_web_responsive/static/src/legacy/scss/big_boxes.scss",
            "/mba_web_responsive/static/src/legacy/scss/list_sticky_header.scss",
            "/mba_web_responsive/static/src/legacy/js/mba_web_responsive.esm.js",
            # "/mba_web_responsive/static/src/legacy/xml/form_buttons.xml",
            "/mba_web_responsive/static/src/legacy/xml/custom_favorite_item.xml",
            "/mba_web_responsive/static/src/components/apps_menu_tools.esm.js",
            "/mba_web_responsive/static/src/components/apps_menu/*",
            "/mba_web_responsive/static/src/components/apps_menu_item/*",
            "/mba_web_responsive/static/src/components/menu_canonical_searchbar/*",
            "/mba_web_responsive/static/src/components/menu_odoo_searchbar/*",
            "/mba_web_responsive/static/src/components/menu_fuse_searchbar/*",
            "/mba_web_responsive/static/src/components/menu_searchbar/*",
            "/mba_web_responsive/static/src/components/hotkey/*",
            "/mba_web_responsive/static/src/components/file_viewer/*",
            # "/mba_web_responsive/static/src/components/chatter/*",
            # "/mba_web_responsive/static/src/components/control_panel/*",
            "/mba_web_responsive/static/src/components/command_palette/*",
            "/mba_web_responsive/static/src/views/form/*",
            # Don't include dark mode files in light mode
            ("remove", "mba_web_responsive/static/src/**/*.dark.scss"),
        ],
        "web.assets_web_dark": [
            "mba_web_responsive/static/src/**/*.dark.scss",
        ],
        "web.assets_clickbot": [
            "/mba_web_responsive/static/src/clickbot/clickbot.esm.js",
        ],
        "web.qunit_suite_tests": [
            "/mba_web_responsive/static/tests/apps_menu_tests.esm.js",
            "/mba_web_responsive/static/tests/apps_menu_search_tests.esm.js",
        ],
    },
    "sequence": 1,
}
