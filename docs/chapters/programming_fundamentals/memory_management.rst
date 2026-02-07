Memory management
=================
We noted in :ref:`computer hardware <computer_hardware>` that memory is often the first bottleneck in a computer system that we run into as we move to writing higher performance code. This motivates some of the choices we make in this course.

This is because memory is a finite resource. We can run out of it if we don't manage memory appropriately. In Electronic Engineering we often work with embedded systems, which may have very limited memory available. Even in larger systems, inefficient use of memory can lead to slow code, and decisions on memory management shape how we do our programming.


An analogy
----------
Imagine we want to drive a number of people from Manchester to London. If we have a fast sports car, we'll probably expect to get there more quickly than if we have an old slow car. (In practice both will be limited by the speed limit and traffic, and so the car model won't make a big difference.) The car is like the processor in the computer. A slower processor might take longer to complete the same task, but it will still get there in the end.

Memory is more like the number of seats in the car. A standard UK car can take 4 passengers. If there are 8 people to take, the car needs to make 3 trips (Manchester to London, back to Manchester, and then again to London). It takes 3 times as long compared to having to take 4 people. 

More, imagine that in London somebody forgets to get out of the car. (Perhaps a bit unlikely, but maybe they fell asleep, or they really like the driver's company!) Now there's only 3 seats free for next trip. There will need to be 5 journeys to get everyone there. If someone forgets to get out of the car every time, eventually there won't be any seats left at all and everything will grind to halt.


Garbage collection
------------------
Computers can automatically manage memory for us, with this generally known as *garbage collection*. The computer will monitor which pieces of memory are still being used by the program, and which are no longer needed. It can then free up memory that is no longer being used, allowing it to be re-used later on. In our analogy above, this is like the driver making sure that the car is empty before starting the return trip.

However, doing garbage collection takes some time, say 100 ms. Also, the computer decides exactly when it's carried out. For the highest performance systems, and in particular real-time embedded systems like we tend to make in electronic engineering, it's hard to accept this unpredictability. A car driving at 70 miles per hour will cover about 3 meters in 100 ms. It can't be ignoring any input from sensors during this time. A small buggy like you'll make in your embedded systems project next year might travel at 1 meter per second, and so would cover 10 cm (a very larger distance compared to the size of the course).


Our choices for this course
---------------------------
If some delays are acceptable in your application while garbage collection is carried out, there are lots of high performance languages such as Java and Go which might be good choices. (100 ms is very small on a human time scale, there are lots of applications where it is perfectly acceptable.) We won't cover these here. 

As we're electronic engineers, we're more focused on real-time or embedded systems applications. We're thus going to look at high performance languages which are not garbage collected. We'll look at languages like C, C++ and Rust, which give the programmer more control over when memory is allocated and freed, at the cost that you, the programmer, is responsible for doing the memory management. We'll see how to do this in the labs. It's a trade-off between programmer effort and control, and performance, and we're going to go for performance. Knowing about stack and heap memory, and pointers, form key parts of memory management. 

