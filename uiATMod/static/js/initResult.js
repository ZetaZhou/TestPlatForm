function infoloop(url) {

    $.get(url, {sign: true}, function (data, status) {

        caseinfo_list = data.caseinfo_list;

        // if (caseinfo_list.length > 0) {
        //     var hwnd_bgi = document.getElementById('bgi');
        //     hwnd_bgi.style.display = 'None';
        // }


        for (var i = 1; i < caseinfo_list.length + 1; i++) {

            var index = caseinfo_list[i - 1].CASE_ID;
            var tr = "<tr class=tr" + index + " style='position: relative'></tr>";
            $(".case_result tbody").append(tr);

            for (var j = 0; j < 10; j++) {
                var td = "<td></td>";
                $(".case_result .tr" + index + ':last-child').append(td);
            }

            var hwnd_caseid = document.querySelectorAll('.tr' + index + ':last-child td:nth-child(1)');
            hwnd_caseid[0].innerHTML = caseinfo_list[i - 1].CASE_ID;

            var hwnd_casename = document.querySelectorAll('.tr' + index + ':last-child td:nth-child(2)');
            hwnd_casename[0].innerHTML = caseinfo_list[i - 1].CASE_NAME_DETAIL;

            var hwnd_modelname = document.querySelectorAll('.tr' + index + ':last-child td:nth-child(3)');
            hwnd_modelname[0].innerHTML = caseinfo_list[i - 1].MODEL_NAME;

            var hwnd_starttime = document.querySelectorAll('.tr' + index + ':last-child td:nth-child(4)');
            hwnd_starttime[0].innerHTML = caseinfo_list[i - 1].STARTTIME;

            var hwnd_endtime = document.querySelectorAll('.tr' + index + ':last-child td:nth-child(5)');
            hwnd_endtime[0].innerHTML = caseinfo_list[i - 1].ENDTIME;

            var hwnd_duration = document.querySelectorAll('.tr' + index + ':last-child td:nth-child(6)');
            hwnd_duration[0].innerHTML = caseinfo_list[i - 1].DURATION;

            var hwnd_owner = document.querySelectorAll('.tr' + index + ':last-child td:nth-child(7)');
            hwnd_owner[0].innerHTML = caseinfo_list[i - 1].CASE_OWNER;

            var hwnd_result = document.querySelectorAll('.tr' + index + ':last-child td:nth-child(8)');
            hwnd_result[0].innerHTML = caseinfo_list[i - 1].TEST_RESULT;


            if (caseinfo_list[i - 1].TEST_RESULT != 'FAILE') {
                var td_hover = "<td class='td_hover_pass' id=td_hover" + sign + "></td>";
                $(".case_result .tr" + index + ':last-child').append(td_hover);
                hwnd_result[0].style.color = "#eb4b8a";
                var img_pass = "<img src ='/static/img/source/pass.png'>";
                $('.tr' + index + ':last-child td:nth-child(10)').append(img_pass);
            }

            else {
                var td_hover = "<td class='td_hover' id=td_hover" + sign + "></td>";
                $(".case_result .tr" + index + ':last-child').append(td_hover);
                var hwnd_tdhover = document.querySelectorAll('#td_hover' + sign);
                var pre = "<pre></pre>";
                $('#td_hover' + sign).append(pre);
                var hwnd_tdhover_pre = document.querySelectorAll('#td_hover' + sign + ' pre');

                hwnd_result[0].style.color = "#4bebb4";
                var img_faile = "<img src ='/static/img/source/faile.png'>";
                $('.tr' + index + ':last-child td:nth-child(10)').append(img_faile);
                hwnd_tdhover_pre[0].innerHTML = caseinfo_list[i - 1].MESSAGE;
            }

            var hwnd_message = document.querySelectorAll('.tr' + index + ':last-child td:nth-child(9)');
            $('.tr' + index + ':last-child td:nth-child(9)').on("mouseover", function () {
                this.parentNode.lastChild.style.display = 'block';
            });
            $('.tr' + index + ':last-child td:nth-child(9)').on("mouseout", function () {
                this.parentNode.lastChild.style.display = 'none';
            });
            if (caseinfo_list[i - 1].MESSAGE.length > 30) {
                hwnd_message[0].innerHTML = caseinfo_list[i - 1].MESSAGE.slice(0, 30);
                hwnd_message[0].innerHTML += '...';
            }
            else {
                hwnd_message[0].innerHTML = caseinfo_list[i - 1].MESSAGE;
            }
            sign += 1;
        }

    });
}

