function custom_template(obj){
            var data = $(obj.element).data();
            var text = $(obj.element).text();
            if(data && data['img_src']){
                img_src = data['img_src'];
                template = $("<div class='dropdown_block' > <img class='drop_img' src=\"" + img_src + "\" /> <p class='drop_p'>" + text + "</p> </div>");
                return template;
            }
        }
    var options = {
        'templateSelection': custom_template,
        'templateResult': custom_template,
    }
    $('#id_select_1').select2(options);
    $('#id_select_2').select2(options);
    $('.select2-container--default .select2-selection--single').css({'height': 'auto', 'margin': '0', 'padding': '0', 'width': '350px'});