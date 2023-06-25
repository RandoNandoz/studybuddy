import data from '../../data/data.json' assert { type: 'json' };
console.log(data);

var listdata = JSON.parse(data);
var listItemString = $('#listItem').html();
listdata.forEach(buildNewList);

function buildNewList(item, index) {
  var listItem = $('<li>' + listItemString + '</li>');
  var listItemTitle = $('.title', listItem);
  listItemTitle.html(item.nask);
  var listItemDuration = $('.duration', listItem);
  listItemDuration.html(item.duration);
  var listItemPriority = $('.priority', listItem);
  listItemPriority.html(item.priority);
  $('#dataList').append(listItem);
}