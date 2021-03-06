<!--HTML-->
<!--Step:1 Prepare a dom for ECharts which (must) has size (width & hight)-->
<!--Step:1 为ECharts准备一个具备大小（宽高）的Dom-->
<div id="chart3_demo" style="height:500px;border:1px solid #ccc;padding:10px;"></div>
<!--JS-->
<!--Step:2 引入echarts.js-->
<script src="https://magicbox.bk.tencent.com/static_api/v3/assets/js/jquery-1.10.2.min.js"></script>
<script src="https://magicbox.bk.tencent.com/static_api/v3/assets/echarts-2.0/echarts-all.js"></script>
<script type="text/javascript">
//chart3_demo_js_start
// Step:3 为模块加载器配置echarts的路径，从当前页面链接到echarts.js，定义所需图表路径

// Step:4 动态加载echarts然后在回调函数中开始使用，注意保持按需加载结构定义图表路径
// standard line chart
function createEStandLineChart(conf){
    var myChart = echarts.init(document.getElementById(conf.selector));
    var legendData = []
    for(var i=0; i < conf.data.series.length;i++){
        legendData.push(conf.data.series[i].name)
    }
    myChart.setOption({
        tooltip : {
            trigger: 'axis'
        },
        legend: {
            y: 'bottom',
            data:legendData
        },
        toolbox: {
            show : true,
            feature : {
                mark : {show: true},
                dataView : {show: true, readOnly: false},
                magicType : {show: true, type: ['bar','line']},
                restore : {show: true},
                saveAsImage : {show: true}
            }
        },
        calculable : true,
        xAxis : [
            {
                type : 'category',
                data : conf.data.xAxis
            }
        ],
        yAxis : [
            {
                type : 'value',
                splitArea : {show : true}
            }
        ],
        series : conf.data.series
    });
 }
function initEStandLineChart(conf){
    $.ajax({
        url: conf.url,
        type: 'GET',
        dataType: conf.dataType,
        success: function(res){
            //获取数据成功
            if (res.result){
                createEStandLineChart({
                    selector: conf.containerId, // 图表容器
                    data: res.data, // 图表数据
                });
            }
        }
    })
}
$(function(){
    initEStandLineChart({
        url: 'https://magicbox.bk.tencent.com/static_api/v3/components/chart3/demo.json',
        dataType: 'json',
        containerId: 'chart3_demo'
    });
});
//chart3_demo_js_end
</script>