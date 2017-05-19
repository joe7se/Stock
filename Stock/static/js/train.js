function train(){	
	var code=$("#code").val();
	var start = $("#start").val();
	var end = $("#end").val();
	$.get("/ENE/train?code="+code+"&start="+start+"&end="+end,function(data,status){
		var dataarray = []
		for(var d in data){
            d = data[d]
            var temp = {}
            temp.upper = d[0]
            temp.lower = d[1]
            temp.days = d[2]
            dataarray.push(temp)
        }
//		obj = JSON.parse(dataarray);
		document.getElementById("m1").innerHTML = dataarray[0].upper;
		alert(dataarray[0].upper);
		document.getElementById("m2").innerHTML = dataarray[0].lower;
		document.getElementById("n").innerHTML = dataarray[0].days;
		
	})
}