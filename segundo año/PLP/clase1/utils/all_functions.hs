foldr :: (a->b->b)->b->[a]->[b]
foldr _ z [] = [z]
foldr f z (x:xs) = f x : foldr f z xs

sumaN :: Int -> [Int] -> [Int]
sumaN _ [] = [] 
sumaN n (x:xs) = (n+x) : sumaN n xs