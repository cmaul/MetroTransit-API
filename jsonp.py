def jsonp(request, data):
    callback = request.get('callback')
    if callback:
        return "%s(%s)" % (callback, data)
    else:
        return data

