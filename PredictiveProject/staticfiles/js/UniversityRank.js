<script>
    window.onload = function () {

    var a = document.getElementById('uor').value;
    var b = document.getElementById('uoa').value;
    var c = document.getElementById('ubc').value;



var chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
	theme: "light2", // "light1", "light2", "dark1", "dark2"
	title:{
        text: "University Ranking based on your profile"
},
	axisY: {
        title: "Acceptance Rate"
},
	data: [{
        type: "column",
    showInLegend: true,
    legendMarkerColor: "grey",
    legendText: "MMbbl = 10 Percent",
    dataPoints: [
    
			{y: parseInt(a), label: "University of Regina" },
			{y: parseInt(b),  label: "University of Alberta" },
			{y: parseInt(c),  label: "University of British Columbia" }
]
}]
});
chart.render();

}
</script>