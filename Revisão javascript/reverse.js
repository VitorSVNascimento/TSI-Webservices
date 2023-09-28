const btn = document.querySelector('#search');
const div_responses = document.querySelector('#response');

document.body.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        search();
    }
});


btn.addEventListener('click', search);

function search(){
    div_responses.innerHTML = ''
    const rua = document.querySelector('#rua');
    const cidade = document.querySelector('#cidade');
    const estado = document.querySelector('#estado');
    req = new XMLHttpRequest();
    req.onloadend = function(){
        resp = req.responseText;
        resp_obj = JSON.parse(resp);
        
        create_cep_table(resp_obj)
        
        
    }
       req.open('GET', 'https://viacep.com.br/ws/'+estado.value+'/'+cidade.value+'/'+rua.value+'/json/');
       req.send(null);


}

function create_cep_table(resp_obj) {
    const table = document.createElement('table');
    
    // Create table headers
    const headerRow = document.createElement('tr');
    const cepHeader = document.createElement('th');
    cepHeader.textContent = 'CEP';
    headerRow.appendChild(cepHeader);
    
    const ruaHeader = document.createElement('th');
    ruaHeader.textContent = 'Rua';
    headerRow.appendChild(ruaHeader);
    
    const cidadeHeader = document.createElement('th');
    cidadeHeader.textContent = 'Cidade';
    headerRow.appendChild(cidadeHeader);
    
    table.appendChild(headerRow);

    let num = 0;
    for (let resp of resp_obj) {
        const tr = document.createElement('tr');
        
        // Apply alternating row colors using CSS
        tr.className = num % 2 === 0 ? 'even' : 'odd';

        const cepCell = document.createElement('td');
        cepCell.textContent = resp['cep'];
        tr.appendChild(cepCell);

        const logradouroCell = document.createElement('td');
        logradouroCell.textContent = resp['logradouro'];
        tr.appendChild(logradouroCell);

        const localidadeCell = document.createElement('td');
        localidadeCell.textContent = resp['localidade'];
        tr.appendChild(localidadeCell);

        table.appendChild(tr);
        num++;
    }
    div_responses.appendChild(table);
}