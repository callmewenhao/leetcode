# 堆
heapq --- 堆队列算法。这个模块提供了堆队列算法的实现，也称为优先队列算法。
该模块实现的堆是**最小堆**，如果需要实现最大堆，可以把元素加负号，这样堆顶的元素就是**最大值的相反数**。


1. heap[0] 表示最小的元素
2. 要创建一个堆，可以使用list来初始化为 []（用一个空list代表这个堆，然后直接使用），或者你可以通过一个函数 heapify() ，来把一个list转换成堆。
3. 建议使用 heapify() 来初始化

## 定义了以下函数

1. `heapq.heappush(heap, item)`

将 item 的值加入 heap 中，保持堆的不变性。

2. `heapq.heappop(heap)`

弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError 。使用 heap[0] ，可以只访问最小的元素而不弹出它。

3. `heapq.heappushpop(heap, item)`

将 item 放入堆中，然后弹出并返回 heap 的最小元素。该组合操作比先调用 heappush() 再调用 heappop() 运行起来更有效率。

4. `heapq.heapify(x)`

将list x 转换成堆，原地，线性时间内。

5. `heapq.heapreplace(heap, item)`

弹出并返回 heap 中最小的一项，同时推入新的 item。 堆的大小不变。 如果堆为空则引发 IndexError。

这个单步骤操作比 heappop() 加 heappush() 更高效，并且在使用固定大小的堆时更为适宜。 pop/push 组合总是会从堆中返回一个元素并将其替换为 item。

返回的值可能会比添加的 item 更大。 如果不希望如此，可考虑改用 heappushpop()。 它的 push/pop 组合会返回两个值中较小的一个，将较大的值留在堆中。

[官方文档](https://docs.python.org/zh-cn/3/library/heapq.html)




