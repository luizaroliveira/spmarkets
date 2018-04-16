'FORMAT: 1A
HOST: http://localhost/

# spmarkets

Restful API to view, manage and filter open markets in São Paulo.

## Markets by id [/api/feiras/123]

### Get Market [GET]

Get market by id.

+ Request (application/json)

+ Response 200 (application/json)

    + Body

            {"id" : -9999,
                "long" : -46625252,
                "lat" : -23592852,
                "setcens" : "355030867000252",
                "areap" : "3550308005182",
                "coddist" : 68,
                "distrito" : "RIO PEQUENO",
                "codsubpref" : 10,
                "subprefe" : "BUTANTA",
                "regiao5" : "Oeste",
                "regiao8" : "Oeste",
                "nome_feira" : "AURIFLAMA",
                "registro" : "9899-5",
                "logradouro" : "RUA DR VIRGILIO ALVIN FRANCO",
                "numero" : "10.000000",
                "bairro" : "JD D ABRIL",
                "referencia" : "RV RAPOSO TAVARES KM 166"
            }

### Delete Market [DELETE]

Delete market by id.

+ Request (application/json)

+ Response 204 (application/json)


## Markets collection [/api/feiras]

### Get Markets [GET]

Returns a list of all markets in the database.
Can be filtered by any field, by using the query parameter.

+ Parameters

    + q: {"filters":[{"name":"distrito", "op": "like", "val": "VILA%"}]} (application/json) - (Optional)
    Query for filtering results. 
    Operators: eq (equals), like.
        
    
+ Response 200 (application/json)

        {
            "num_results": 1,
            "objects": [
                {
                    "areap": "3550308005182",
                    "bairro": "JD D ABRIL",
                    "coddist": 68,
                    "codsubpref": 10,
                    "distrito": "RIO PEQUENO",
                    "id": -9999,
                    "lat": -23592852,
                    "logradouro": "RUA DR VIRGILIO ALVIN FRANCO",
                    "long": -46625252,
                    "nome_feira": "AURIFLAMA",
                    "numero": "10.000000",
                    "referencia": "RV RAPOSO TAVARES KM 166",
                    "regiao5": "Oeste",
                    "regiao8": "Oeste",
                    "registro": "9899-5",
                    "setcens": "355030867000252",
                    "subprefe": "BUTANTA"
                }
            ],
            "page": 1,
            "total_pages": 1
        }

### Create Market [POST]

Create a new market.

+ Request (application/json)

        {
            "id" : -9999,
            "long" : -46625252,
            "lat" : -23592852,
            "setcens" : "355030867000252",
            "areap" : "3550308005182",
            "coddist" : 68,
            "distrito" : "RIO PEQUENO",
            "codsubpref" : 10,
            "subprefe" : "BUTANTA",
            "regiao5" : "Oeste",
            "regiao8" : "Oeste",
            "nome_feira" : "AURIFLAMA",
            "registro" : "9899-5",
            "logradouro" : "RUA DR VIRGILIO ALVIN FRANCO",
            "numero" : "10.000000",
            "bairro" : "JD D ABRIL",
            "referencia" : "RV RAPOSO TAVARES KM 166"
        }

+ Response 201 (application/json)


    + Body

            {"id" : -9999,
                "long" : -46625252,
                "lat" : -23592852,
                "setcens" : "355030867000252",
                "areap" : "3550308005182",
                "coddist" : 68,
                "distrito" : "RIO PEQUENO",
                "codsubpref" : 10,
                "subprefe" : "BUTANTA",
                "regiao5" : "Oeste",
                "regiao8" : "Oeste",
                "nome_feira" : "AURIFLAMA",
                "registro" : "9899-5",
                "logradouro" : "RUA DR VIRGILIO ALVIN FRANCO",
                "numero" : "10.000000",
                "bairro" : "JD D ABRIL",
                "referencia" : "RV RAPOSO TAVARES KM 166"
            }
            
### Update Market [PATCH]

Update market. The only field not available for update is id.

+ Request (application/json)

        {
            "coddist" : 68,
            "referencia" : "RV RAPOSO TAVARES KM 166"
        }

+ Response 200 (application/json)


    + Body

            {"id" : -9999,
                "long" : -46625252,
                "lat" : -23592852,
                "setcens" : "355030867000252",
                "areap" : "3550308005182",
                "coddist" : 68,
                "distrito" : "RIO PEQUENO",
                "codsubpref" : 10,
                "subprefe" : "BUTANTA",
                "regiao5" : "Oeste",
                "regiao8" : "Oeste",
                "nome_feira" : "AURIFLAMA",
                "registro" : "9899-5",
                "logradouro" : "RUA DR VIRGILIO ALVIN FRANCO",
                "numero" : "10.000000",
                "bairro" : "JD D ABRIL",
                "referencia" : "RV RAPOSO TAVARES KM 166"
            }

