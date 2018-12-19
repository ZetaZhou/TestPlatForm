function inittree_datatemp(url) {
    var result_data = 0;
    $.ajax({
        type: "get",
        url: url,
        async: false,
        success: function (data) {
            // alert(data.treeinfo);
            // console.log(data);
            result_data = data.treeinfo
        }
    });
    return result_data;
}