# Utility functions
def form_to_dictionary(form):
    json = { }
    for fieldname, value in form.data.items():
        json[fieldname] = value
    return json

