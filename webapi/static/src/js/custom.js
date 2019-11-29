$(document).ready(function(){
    
    $('#selectloaivanbang').select2({
        theme: 'bootstrap4'
    })
    $('#selectcosodaotao').select2({
        theme: 'bootstrap4'
    })

    $('#reservation').daterangepicker({
        locale: {
            format: 'YYYY-M-DD',
        }
    })
    



    $('#form_tracuu').submit(function(){
        
        var hoten = $('#hoten').val();
        var cmnd = $('#chungminhthu').val();
        var loaivanbang = $('#selectloaivanbang').val();
        var cosodaotao = $('#selectcosodaotao').val();
        var namcapbang = $('#namcapbang').val();
        var sohieu = $('#sohieu').val();

        var url = '/api/vanbang/?';
        if (hoten){
            url += 'hoten_icontains=' + hoten + '&';
        }
        if (cmnd){
            url += 'cmnd_icontains=' + cmnd + '&';
        }
        if (loaivanbang){
            url += 'loai_vanbang=' + loaivanbang + '&';
        }
        if (cosodaotao){
            url += 'cosodaotao=' + cosodaotao + '&';
        }
        if (namcapbang){
            url += 'ngaycapbang_year=' + namcapbang + '&';
        }
        if (sohieu){
            url += 'sohieu=' + sohieu + '&';
        }
        // '/api/vanbang/?hoten_icontains='+ hoten + '&loai_vanbang=' + loaivanbang + '&cosodaotao=' + cosodaotao + '&cmnd_icontains=' + cmnd + '&ngaycapbang_year=' + namcapbang + '&sohieu=' + sohieu
        $.ajax({
            url: url ,
            method: 'GET',
            contentType: 'application/json',
            success: function(response){
                $('tbody#content_data').empty()
                if (response.count > 0){
                    for (var i = 0; i < response.results.length; i++){
                        record = response.results[i]
                        var $row = $('<tr>');
                        $row.append('<td>'+ (i+1) +'</td>');
                        $row.append('<td>'+ record.hoten +'</td>');
                        $row.append('<td>'+ record.ngaysinh +'</td>');
                        $row.append('<td>'+ record.gioitinh_display +'</td>');
                        $row.append('<td>'+ record.chuyennganh +'</td>');
                        $row.append('<td>'+ record.xeploai_display +'</td>');
                        $row.append('<td>'+ record.ngaycapbang +'</td>');
                        $('tbody#content_data').append($row);
                    }
                } else {
                    alert('Không tìm thấy thông tin văn bằng!\nVui lòng kiểm tra lại thông tin tra cứu :)')
                }
            },
        });
        $('button#submit').remove();
        $('#reset').append('<button class="btn btn-danger" onClick="window.location.reload();">Làm mới</button>')
        event.preventDefault();
    })

    $('#form_filter').submit(function(){

        var loaivanbang = $('#selectloaivanbang').val();
        var rangedate = $('#reservation').val();
        var start_date = rangedate.split(' - ')[0]
        var end_date = rangedate.split(' - ')[1]
        var url = '/api/vanbang/?';
        if (loaivanbang != 'false'){
            url += 'loai_vanbang=' + loaivanbang + '&';
        }
        url += 'start_date='+ start_date + '&end_date=' + end_date;
        $.ajax({
            url: url,
            method: 'GET',
            contentType: 'application/json',
            success: function(response){
                $('tbody#content_data').empty();
                $('#button_report').empty();
                if (response.count > 0){
                    for (var i = 0; i < response.results.length; i++){
                        record = response.results[i]
                        var $row = $('<tr>');
                        $row.append('<td>'+ (i+1) +'</td>');
                        $row.append('<td>'+ record.hoten +'</td>');
                        $row.append('<td>'+ record.ngaysinh +'</td>');
                        $row.append('<td>'+ record.cmnd +'</td>');
                        $row.append('<td>'+ record.loai_vanbang_name +'</td>');
                        $row.append('<td>'+ record.cosodaotao_name +'</td>');
                        $row.append('<td>'+ record.ngaycapbang +'</td>');
                        $row.append('<td>'+ record.xeploai_display +'</td>');
                        $('tbody#content_data').append($row);
                    }
                    $button = $('<a href="/api/export/xls/?loaivanbang='+ loaivanbang +'&start_date='+ start_date +'&end_date='+ end_date +'" target="_blank" class="btn btn-success">In báo cáo</a>')
                    $('#button_report').append($button);
                }else {
                    alert('Không tìm thấy thông tin văn bằng!')
                }
            },
        });
        event.preventDefault();
    })

})