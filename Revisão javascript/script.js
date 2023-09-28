const btn = document.querySelector('#search')

btn.onclick = function(){
    var cep = document.querySelector('#cep')
    console.log('teste')
    req = new XMLHttpRequest()
    req.onloadend = function(){
        resp = req.responseText;
        resp_obj = JSON.parse(resp);
        alert('O CEP ' + resp_obj['cep'] + ' pertence à rua ' +
        resp_obj['logradouro']);
       }
       req.open('GET', 'https://viacep.com.br/ws/'+cep.value+'/json/');
       req.send(null);

}