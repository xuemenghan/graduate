
/**
 * 
 * create time: 2018-09-19
 *
 * 该文件只用于测试demo使用,实际开发中,请不要引用该文件
 *
 * 
 *
 */


/**
 * reset common request function 
 * action: POST => GET
 */
root.request = function (api, param, func) {
	var _url = '/demo_manage' + api;
	$.get(_url, function(data){
		if(typeof data == 'string'){
			data = eval('('+data+')');
		}
		if(func) func(data);
	});
}
