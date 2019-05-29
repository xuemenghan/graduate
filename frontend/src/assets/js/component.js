
$(function () {

	// 初始化页面内容
	var hash = root.formatHash().hash;
	if(hash){
		var _url = SITE_URL + hash.join("/");
		$("#content").load(_url);
	}

	$(window).on("hashchange", function() {//兼容ie8+和手机端
        var hash = root.formatHash().hash;
		if(hash){
			var _url = SITE_URL + hash.join("/");
			$("#content").load(_url);
		}
    });

	// 加载默认内容模板
	$("div[data-url]").each(function () {
		var _this = $(this);
		if(_this.attr("id") != "content" || !hash) {
			var _template = _this.data("url");
			var _url = SITE_URL + _template;
			_this.load(_url);
		}
	});

	// 重置a标签打开页面
	// $("body").on("click", "a", function (e) {
	// 	var _this = $(this);
	// 	if (!_this.hasClass("sync")){
	// 		var _href = SITE_URL + _this.attr("href");
	// 		$("#content").load(_href);
	// 	}
	// });
});