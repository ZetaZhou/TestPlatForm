var pageNumber = 10;          //一页显示多少条数据
var arrayLength = 5;          //多少页码形成一组
var totalPage = 1;   			//总共的页码数
var indexPage = 1;   			//当前的页码数
var totalArrayPage = 1;    	//共多少组页码

//初始化table表格
function inittable() {

    for (var i = 0; i < pageNumber; i++) {

        var tr = "<tr id=tr" + i + "></tr>";
        $("#case_table tbody").append(tr);

        // var td0 = "<td><input type='checkbox' name='selected' value= value" + i + " onclick=casecheck(this)></td>";

        var td0 = '<td><label for= control' + i + '>' +
            '<img onclick=casecheck(this)  src="/static/img/checkbox_0.gif" value = value' + i + ' name="selected"></label>' +
            '<input type="checkbox" style="display:none" id=control' + i + ' class="selected"></td>';
        $("#case_table #tr" + i).append(td0);

        var td1 = "<td class='caseid' ></td>";
        var td2 = "<td class='modulename' ></td>";
        var td3 = "<td class='casename' ></td>";
        var td4 = "<td class='addr'></td>";
        $("#case_table #tr" + i).append(td1, td2, td3, td4);
    }
}

// 清空casetable
function clear_table(caseid_list) {

    for (var i = 0; i < caseid_list.length; i++) {
        chkbox_list[i].checked = false;
        chkboximg_list[i].src = '/static/img/checkbox_0.gif';
        caseid_list[i].innerHTML = '';
        casename_list[i].innerHTML = '';
        modulename_list[i].innerHTML = '';
        addr_list[i].innerHTML = '';
    }
}

function set_table(case_list) {

    for (var i = 0; i < case_list.length; i++) {
        chkbox_list[i].checked = case_list[i][2];
        if (chkbox_list[i].checked) {
            chkboximg_list[i].src = '/static/img/checkbox_1.gif';
        }
        else {
            chkboximg_list[i].src = '/static/img/checkbox_0.gif';
        }
        caseid_list[i].innerHTML = case_list[i][0];
        casename_list[i].innerHTML = case_list[i][4];
        modulename_list[i].innerHTML = case_list[i][3];
        addr_list[i].innerHTML = case_list[i][1];
    }
}


//查询时触发事件
function selectAllnum(totlenum) {

    //输入值是否为完整的年月日时间
    //判断结束时间是否大于开始时间
    //通过ajax获取数据，

    var totalcaseNumber = totlenum;
    totalPage = Math.ceil(totalcaseNumber / pageNumber);
    totalArrayPage = Math.ceil(totalPage / arrayLength);

    //在页面上设置总页数和结果总数量
    $(".showSection .showMore .totalNumber").text("共" + totalcaseNumber + "条");
    $(".showSection .showMore .totalPage").text("共" + totalPage + "页");

    //设置尾页的值
    $(".showSection .showMore span.after span:last-child").attr("mark", totalPage);
    console.log("页码数为：" + totalPage);
    setInput();
}

//分组页码显示
function setInput() {

    //防止当前页码大于最大页码
    if (indexPage > totalPage) {
        indexPage = totalPage;
    }

    //防止当前页码小于1
    if (indexPage < 1) {
        indexPage = 1;
    }

    var htmlCode = "";
    var indexArrayPage = Math.ceil(indexPage / arrayLength);    	//当前下标是第几组页码
    var beforeArrayPage = 0;      //倒数第二组的第一个下标
    var afterArrayPage = 0;

    //控制首页、上一页;下一页、尾页的显示和隐藏
    $(".showSection .showMore span.input").removeClass("hidden");
    if (indexPage == 1) {
        $(".showSection .showMore span.before").addClass("hidden");
    } else if (indexPage == totalPage) {
        $(".showSection .showMore span.after").addClass("hidden");
    } else {

    }

    //控制上一页、下一页中的值
    $(".showSection .showMore span.before span:last-child").attr("mark", (indexPage - 1));
    $(".showSection .showMore span.after span:first-child").attr("mark", (indexPage + 1));

    //控制页码的展示
    if (totalPage <= arrayLength) {
        for (var i = 1; i <= totalPage; i++) {
            htmlCode += '<span  onclick="servlet(this)" mark="' + i + '">' + i + '</span>';
        }
        $(".showSection .showMore>span.content").html(htmlCode);
    } else {
        if (indexArrayPage == 1) {
            for (var i = 1; i <= arrayLength; i++) {
                htmlCode += '<span  onclick="servlet(this)" mark="' + i + '">' + i + '</span>';
            }
            htmlCode += '<span  onclick="servlet(this)" mark="' + (arrayLength + 1) + '">...</span>';
            $(".showSection .showMore>span.content").html(htmlCode);
        } else if (indexArrayPage == totalArrayPage) {
            beforeArrayPage = (totalArrayPage - 1) * arrayLength;
            htmlCode += '<span onclick="servlet(this)" mark="' + beforeArrayPage + '">...</span>';
            for (var i = (beforeArrayPage + 1); i <= totalPage; i++) {
                htmlCode += '<span onclick="servlet(this)" mark="' + i + '">' + i + '</span>';
            }
            $(".showSection .showMore>span.content").html(htmlCode);
        } else {
            beforeArrayPage = (indexArrayPage - 1) * arrayLength;
            afterArrayPage = indexArrayPage * arrayLength + 1;
            htmlCode += '<span onclick="servlet(this)" mark="' + beforeArrayPage + '">...</span>';
            for (var i = (beforeArrayPage + 1); i < afterArrayPage; i++) {
                htmlCode += '<span onclick="servlet(this)" mark="' + i + '">' + i + '</span>';
            }
            htmlCode += '<span onclick="servlet(this)" mark="' + afterArrayPage + '">...</span>';
            $(".showSection .showMore>span.content").html(htmlCode);
        }
    }
}