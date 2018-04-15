import json

get = {'url': '/api/feira'}

# Good post request
successful_post = dict(url='/api/feira', data=json.dumps(
    dict(id=-9999, long=-46625252, lat=-23592852, setcens="355030867000252", areap="3550308005182", coddist=68,
         distrito="RIO PEQUENO", codsubpref=10, subprefe="BUTANTA", regiao5="Oeste", regiao8="Oeste",
         nome_feira="AURIFLAMA", registro="9899-5", logradouro="RUA DR VIRGILIO ALVIN FRANCO", numero="10.000000",
         bairro="JD D ABRIL", referencia="RV RAPOSO TAVARES KM 166")))

# Missing required field
unsuccessful_post = dict(url='/api/feira', data=json.dumps(
    dict(id=-9999, long=-46625252, lat=-23592852, setcensss="355030867000252", areap="3550308005182", coddist=68,
         distrito="RIO PEQUENO", codsubpref=10, subprefe="BUTANTA", regiao5="Oeste", regiao8="Oeste",
         nome_feira="AURIFLAMA", registro="9899-5", logradouro="RUA DR VIRGILIO ALVIN FRANCO", numero="10.000000",
         bairro="JD D ABRIL", referencia="RV RAPOSO TAVARES KM 166")))


update = dict(url='/api/feira/-9999', data=json.dumps({"bairro": "JD D MARCO"}))

bad_update = dict(url='/api/feira/-9999', data=json.dumps({"id": "-9998"}))

delete = dict(url='/api/feira/-9999')

search_district_like = dict(url='/api/feira?q={"filters":[{"name":"distrito", "op": "like", "val": "%MADALENA"}]}')

search_name_equals = dict(url='/api/feira?q={"filters":[{"name":"nome_feira", "op": "eq", "val": "VILA MEDEIROS"}]}')
