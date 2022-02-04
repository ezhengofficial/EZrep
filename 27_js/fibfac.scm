#lang racket
(define factorial
  (lambda(n)
    (if (= n 1)
        1
        ( * n (factorial (- n 1)))
     )
   )
 )

(factorial 5)
(factorial 6)
(factorial 7)

(define fib
  (lambda(n)
    (if (<= n 1)
        1
        (+ (fib(- n 1)) (fib(- n 2)))
        )
    )
  )

(fib 4)