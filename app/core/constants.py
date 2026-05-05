# --------------------------------------------------
# CONFIGURAÇÃO CENTRAL DOS MÓDULOS
# --------------------------------------------------

MODULES = [
    {
        "name": "Administração",
        "route": "/admin",
        "key": "admin",
        "icon": "01",
        "show_in_sidebar": True
    },
    {
        "name": "Comercial",
        "route": "/comercial",
        "key": "comercial",
        "icon": "02",
        "show_in_sidebar": True
    },
    {
        "name": "Financeiro",
        "route": "/financeiro",
        "key": "financeiro",
        "icon": "03",
        "show_in_sidebar": True
    },
    {
        "name": "Processos",
        "route": "/processos",
        "key": "processos",
        "icon": "04",
        "show_in_sidebar": True
    },
    {
        "name": "Produção",
        "route": "/producao",
        "key": "producao",
        "icon": "05",
        "show_in_sidebar": True
    },
]

# --------------------------------------------------
# MAPAS AUTOMÁTICOS
# --------------------------------------------------

ROUTES = {m["key"]: m["route"] for m in MODULES}
PAGE_LABELS = {m["route"]: m["name"] for m in MODULES}

# --------------------------------------------------
# ADMIN
# --------------------------------------------------

ADMIN_USERNAME = "ana.processos"

# --------------------------------------------------
# PERMISSÕES
# --------------------------------------------------

ALL_PAGES_OPTIONS = [
    {"label": m["name"], "value": m["route"]}
    for m in MODULES
]