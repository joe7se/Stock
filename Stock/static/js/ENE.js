function train(){
	var code=$("#code").val();
	var start = $("#start").val();
	var end = $("#end").val();
	$.get("/ENE/train?code="+code+"&start="+start+"&end="+end,function(data,status){
		dataArray = [];
		var i=0;
		for(var d in data){
			d = data[i];
			
			i++;
			var temp = {}
			temp.upper = d.upper
			temp.lower = d.lower
			temp.days = d.days
//			alert(temp.upper)
			dataArray.push(temp)
		}
//		alert(dataArray);
//		$('#title').append('<h4>最优参数</h4>');
		$('#bestPara').bootstrapTable({
			striped: true,
        	sidePagination: "client",
//        	pagination:true,
//        	showPaginationSwitch:true,
        	pageNumber: 1,
        	pageSize: 10,
        	pageList: [10, 25, 50, 100],
        	clickToSelect: true,
        	columns: [{
            	field: 'upper',
            	title: 'M1',
           		width:150
        	}, {
            	field: 'lower',
            	title: 'M2',
            	width:150
       	 	}, {
       	 		field: 'days',
            	title: 'N',
            	width:150
       	 	}],
       	 	
        	data: dataArray 
		});
		$('#bestPara').bootstrapTable("load",dataArray);
		
	})
}

$("#selectGroup").change(function(){
    var opt=$("#selectGroup").val();
//    alert(opt);
    if(opt=="1"){
    	stocks=[{
            id: 'sh601998',
            name: '中国银行'
        }, {
            id: 'sh601998',
            name: '中国银行'
        }, {
            id: 'sh601998',
            name: '中国银行'
        }, {
            id: 'sh601998',
            name: '中国银行'
        }];
    }else if(opt=="2"){
    	stocks=[{
            id: 'sh600000',
            name: '中国银行'
        }, {
            id: 'sh600000',
            name: '中国银行'
        }, {
            id: 'sh600000',
            name: '中国银行'
        }, {
            id: 'sh600000',
            name: '中国银行'
        }];
    }else{
    	stocks=[{
            id: 'sh600001',
            name: '中国银行'
        }, {
            id: 'sh600001',
            name: '中国银行'
        }, {
            id: 'sh600001',
            name: '中国银行'
        }, {
            id: 'sh600001',
            name: '中国银行'
        }];
    }
//    $('#stockGroups').append('<h4>股票组'+opt+'</h4>');
    $('#tablepool').bootstrapTable({
        striped: true,
        sidePagination: "client",
//        showPaginationSwitch:true,
        pageNumber: 1,
        pageSize: 10,
        pageList: [10, 20, 30],
        clickToSelect: true,
        columns: [{
            field: 'id',
            title: '股票代码'
        }, {
            field: 'name',
            title: '股票名称'
        }],
        data: stocks
        
    });
    $('#tablepool').bootstrapTable("load",stocks);
});