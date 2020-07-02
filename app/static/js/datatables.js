console.log('aaaaa');
var data = JSON.parse('{{desenho | tojson | safe}}')
var table = $('#data-table').DataTable({});
var span = $('#rpi').text(data.numero_rpi[0])



function dataAdd(data) {
    $.each(data.numero_do_pedido, function (i, key) {
        id_html = guidGenerator();
        table.row.add([
            data.numero_rpi[i],
            data.codigo[i],
            data.numero_do_pedido[i],
            data.nome_do_depositante[i],
            data.nome_do_autor[i],
            data.nome_do_procurador[i],
            data.email[i],
            `
            <form id="${id_html}">
            <input name="email"><input type="hidden" value="${$('#rpi')[0].innerHTML}" name="rpi">
            <input type="hidden" value="${data.numero_do_pedido[i]}" name="num_ped">
            <button type="button" class="btn btn-primary" onclick="post_email('${id_html}')">Inserir</button>
            </form>
            `
        ]);
    });

    table.draw();
};
dataAdd(data);