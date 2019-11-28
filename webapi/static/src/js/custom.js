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
        $.ajax({
            url: '/api/verifying/',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: {
                response: localStorage.res_capcha,
            },
            success: function(response){
                if (response.success){
                    var hoten = $('#hoten').val();
                    var cmnd = $('#chungminhthu').val();
                    var loaivanbang = $('#selectloaivanbang').val();
                    var cosodaotao = $('#selectcosodaotao').val();
                    var namcapbang = $('#namcapbang').val();
                    var sohieu = $('#sohieu').val();
        
                    $.ajax({
                        url: '/api/vanbang/?hoten_icontains='+ hoten + '&loai_vanbang=' + loaivanbang + '&cosodaotao=' + cosodaotao + '&cmnd_icontains=' + cmnd + '&ngaycapbang_year=' + namcapbang + '&sohieu=' + sohieu ,
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
                                    $row.append('<td>'+ record.gioitinh +'</td>');
                                    $row.append('<td>'+ record.chuyennganh +'</td>');
                                    $row.append('<td>'+ record.xeploai +'</td>');
                                    $row.append('<td>'+ record.ngaycapbang +'</td>');
                                    $('tbody#content_data').append($row);
                                }
                            } else {
                                alert('Không tìm thấy thông tin văn bằng!\nVui lòng kiểm tra lại thông tin tra cứu :)')
                            }
                        },
                    });
                } else {
                    alert('Vui lòng xác thực!')
                }
                event.preventDefault();
            },
            error: function(){
                alert('Vui lòng xác thực!');
                event.preventDefault();
            }
        })
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
                        $row.append('<td>'+ record.loai_vanbang +'</td>');
                        $row.append('<td>'+ record.cosodaotao +'</td>');
                        $row.append('<td>'+ record.ngaycapbang +'</td>');
                        $row.append('<td>'+ record.xeploai +'</td>');
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