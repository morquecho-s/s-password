from backend.conection import adminDB as DB

HEAD = "HEAD" # /
TYPE = 'type'
DIR_TO_EXPORT = 'dir_to_export'
GET = 'get'
POST = 'post'
DELETE = 'delete'
EXPORT = 'export'

CONTENT = "CONTENT" # /
EMAIL = "email"
PASSWORD = "password"
GROUP = "group"
ID = "id"

template_request = {
    HEAD:{
        TYPE:None, # -> get||post||delete
        DIR_TO_EXPORT:None, # -> solo es necesario si (TYPE == EXPORT) es Verdaderos
    },
    CONTENT:{
        EMAIL:None,
        PASSWORD:None,
        GROUP:None,
        ID:"None"
    }
}

def check_errors_in_request(request)->tuple[bool,str]:
    ## first check
    if not HEAD in request:
        return (False,"Not HEAD in your request")
    if not CONTENT in request:
        return (False,"Not CONTENT in your request")
    
    if not request[HEAD][TYPE] == EXPORT:
    
        ## second check
        if not TYPE in request[HEAD]:
            return (False,"Not type in your HEAD request")
        
        if (not EMAIL in request[CONTENT]) or (not PASSWORD in request[CONTENT]) or (not GROUP in request[CONTENT]):
            return (False,"Not email or password or group in your request")
        
        ## Three check
        if  not isinstance(request[HEAD][TYPE],str):
            return (False,"Invalid value for HEAD/type in your request. Only accept strings")
        
        for key in request[CONTENT]:
            if not request[CONTENT][key] in [ID,]:
                if not isinstance(request[CONTENT][key],str):
                    return (False,f"Invalid value for {key} in your request. Only accept strings")

    return (True,"all its ok")


def create_frame(request:dict)->str:
    # result = check_errors_in_request(request)
    
    content_request = request[CONTENT]
    try:
        DB.torres.add_frame(content_request[EMAIL],content_request[PASSWORD],content_request[GROUP])
        return "all its ok"
    except Exception as e:
        return e
    
        

def delete_frame(request:dict)->str:
    content_request = request[CONTENT]
    try:
        options = [content_request[EMAIL],content_request[PASSWORD],content_request[GROUP]]
        if not content_request[ID] == "None":
            options.append(int(content_request[ID]))

        DB.torres.delete_frame(*options)
        # print(DB.torres.delete_frame(content_request["id"]))
        return "all its ok"
    except Exception as e:
        return e
    

def get_frames()->list:
    try:
        return DB.torres.get_frames()
    except Exception as e:
        return e
    
def export_frames_in_htmlTable(request)->str:
    try:
        head_request = request[HEAD]
        DB.torres.exportActualTable(head_request[DIR_TO_EXPORT])
    except Exception as e:
        return e



def request(request:dict)->str|list:
    all_ok,result = check_errors_in_request(request)
    if all_ok is True:
        if request[HEAD][TYPE] == POST:
            result = create_frame(request)
        elif request[HEAD][TYPE] == DELETE:
            result = delete_frame(request)
        elif request[HEAD][TYPE] == GET:
            result = get_frames()
        elif request[HEAD][TYPE] == EXPORT:
            result = export_frames_in_htmlTable(request)

    return result