
from typing import  Optional , List
from fastapi import APIRouter, Header , Cookie,Form
from fastapi.responses import Response, HTMLResponse, PlainTextResponse


router = APIRouter(prefix='/product', tags=['product'])

products = ['watch', 'camera', 'phone']

@router.post('/new')
def create_product(name : str = Form(...)):
    products.append(name)
    return products

@router.post('/all')
def get_all_product():
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key='test_cookie' , value='some cookies here ')
    return response

@router.get('/withheader')
def get_products(
    response: Response, 
    custom_header: Optional[List[str]] = Header(None),
    test_cookie: Optional[str]= Cookie(None)
    ):
    if custom_header:
        response.headers['custom_response_headers'] = " and ".join(custom_header)
    return {
        'data':products,
        'custom_header' : custom_header,
        'cookies' : test_cookie
    }

@router.get('/{id}', responses={
    200 : {
        "content":{
        "text/html":{
            "example" : "<div>Product</div>"
        }
    },
    "description": "Returns the HTML Response for an Object"
    },
    404 : {
        "content":{
        "text/plain":{
            "example":"Product Not Found"
        }
    },
    "description": "Clear text Error Message"
    }
})
def get_product_by_id(id: int):
    # error handling & returning two types of response
    out = "Product Not Available"
    if(id > len(products)):
        return PlainTextResponse(content=out, media_type="text/plain")
    else:
        product = products[id]
        out = f"""
        <head>
        <style>
        .product{{
        text-align: center;
        height: 500px;
        width: 30px;
        background-color: lightblue;
        border: 2px solid green ;
        }}
        </style>
        </head>
        <div class="product">{product}</div>
        """
        return HTMLResponse(content=out, media_type="text/html")
