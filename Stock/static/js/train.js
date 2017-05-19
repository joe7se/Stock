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
			alert(temp.upper)
			dataArray.push(temp)
		}
		alert(dataArray);
		$('#title').append('<h4>最优参数</h4>');
		$('#bestPara').bootstrapTable({
			striped: true,
        	sidePagination: "client",
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
            	title: 'days',
            	width:150
       	 	}],
       	 	
        	data: dataArray 
		});
		$('#bestPara').bootstrapTable("load",dataArray);
		
	})
}