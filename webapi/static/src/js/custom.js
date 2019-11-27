$(document).ready(function(){
    
    $('#selectloaivanbang').select2({
        theme: 'bootstrap4'
    })
    $('#selectcosodaotao').select2({
        theme: 'bootstrap4'
    })

    $('#form_tracuu').submit(function(){

        var hoten = $('#hoten').val();
        var cmnd = $('#chungminhthu').val();
        var loaivanbang = $('#selectloaivanbang').val();
        var cosodaotao = $('#selectcosodaotao').val();
        var namcapbang = $('#namcapbang').val();
        var sohieu = $('#sohieu').val();

        $.ajax({
            url: '/api/vanbang/?hoten_icontains='+ hoten + '&loai_vanbang=' + loaivanbang + '&cosodaotao=' + cosodaotao + '&cmnd_icontains=' + cmnd + '&namcapbang=' + namcapbang + '&sohieu=' + sohieu ,
            method: 'GET',
            contentType: 'application/json',
            success: function(response){
                console.log(response)
                if (response.count > 0){
                    
                }
            },
        });
        event.preventDefault();
    })


})