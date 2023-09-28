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

    try {
        const req = new XMLHttpRequest();
        req.onloadend = function () {
            if (req.status === 200) {
                const resp = req.responseText;
                const resp_obj = JSON.parse(resp);
                create_cep_table(resp_obj);
            } else {
                handleError("Falha ao fazer requisição: " + req.status);
            }
        };
        req.onerror = function () {
            handleError("Falha ao fazer a requisição");
        };
        req.open('GET', 'https://viacep.com.br/ws/' + estado.value + '/' + cidade.value + '/' + rua.value + '/json/');
        req.send(null);
    } catch (error) {
        handleError("Ocorreu um erro: " + error.message);
    }



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

function handleError(errorMessage) {
    const errorDiv = document.createElement('div');
    errorDiv.textContent = errorMessage;
    errorDiv.style.color = 'red';
    div_responses.appendChild(errorDiv);
}