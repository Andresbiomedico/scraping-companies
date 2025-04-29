# IDs y XPaths de elementos en la página de la DIAN
ELEMENT_IDS = {
    'nit_input': "vistaConsultaEstadoRUT:formConsultaEstadoRUT:numNit",
    'razon_social': "vistaConsultaEstadoRUT:formConsultaEstadoRUT:razonSocial",
    'dv': "vistaConsultaEstadoRUT:formConsultaEstadoRUT:dv",
    'primer_apellido': "vistaConsultaEstadoRUT:formConsultaEstadoRUT:primerApellido",
    'segundo_apellido': "vistaConsultaEstadoRUT:formConsultaEstadoRUT:segundoApellido",
    'primer_nombre': "vistaConsultaEstadoRUT:formConsultaEstadoRUT:primerNombre",
    'otros_nombres': "vistaConsultaEstadoRUT:formConsultaEstadoRUT:otrosNombres",
    'estado': "vistaConsultaEstadoRUT:formConsultaEstadoRUT:estado",
    'search_button': "vistaConsultaEstadoRUT:formConsultaEstadoRUT:btnBuscar",
    'captcha': "cf-turnstile-response"
}

XPATH_EXPRESSIONS = {
    'fecha': "//td[@class='tipoFilaNormalVerde' and contains(text(), '-')]",
    'observacion': "//td[@class='fondoTituloLeftAjustado' and contains(text(), 'Registro')]",
    'not_registered': "//td[contains(text(), 'No está inscrito en el RUT')]"
}

# Columna que contiene el NIT en el archivo Excel
NIT_COLUMN = 'NIT'