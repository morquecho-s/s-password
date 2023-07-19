from backend.conection import adminDB as DB

template_request = {
    "HEAD":{
        "type":None, # -> get||post||delete
    },
    "CONTENT":{
        "email":None,
        "password":None,
        "group":None
    }
}

def check_errors_in_request(request)->tuple[bool,str]:
    ## first check
    if not "HEAD" in request:
        return (False,"Not HEAD in your request")
    if not "CONTENT" in request:
        return (False,"Not CONTENT in your request")
    
    ## second check
    if not "type" in request["HEAD"]:
        return (False,"Not type in your HEAD request")
    
    if (not "email" in request["CONTENT"]) or (not "password" in request["CONTENT"]) or (not "group" in request["CONTENT"]):
        return (False,"Not email or password or group in your request")
    
    ## Three check
    if  not isinstance(request['HEAD']["type"],str):
        return (False,"Invalid value for HEAD/type in your request. Only accept strings")
    
    for key in request['CONTENT']:
        if not isinstance(request['CONTENT'][key],str):
            return (False,f"Invalid value for {key} in your request. Only accept strings")

    return (True,"all its ok")


def create_frame(request:dict)->str:
    # result = check_errors_in_request(request)
    
    content_request = request["CONTENT"]
    try:
        DB.torres.add_frame(content_request['email'],content_request['password'],content_request['group'])
        return "all its ok"
    except Exception as e:
        return e
    
        

def delete_frame(request:dict)->str:
    content_request = request["CONTENT"]
    try:
        DB.torres.delete_frame(content_request['email'],content_request['password'],content_request['group'])
        # print(DB.torres.delete_frame(content_request["id"]))
        return "all its ok"
    except Exception as e:
        return e
    

def get_frames()->list:
    try:
        return DB.torres.get_frames()
    except Exception as e:
        return e

def request(request:dict)->str:
    all_ok,result = check_errors_in_request(request)
    if all_ok is True:
        if request["HEAD"]["type"] == "post":
            result = create_frame(request)
        elif request["HEAD"]["type"] == "delete":
            result = delete_frame(request)
        elif request["HEAD"]["type"] == "get":
            result = get_frames()

    return result