import collections

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        #This is your starting point. You assume the theater is empty and you start with a perfect score

        # seat 1 and 10 are useless
        total_families=n*2

        # This is a Dictionary. It is grouped by row. If you give me a Row number, I will give you the Taken Seats.

        seat_taken_by_row=collections.defaultdict(set)
        # When you use collections.defaultdict(), you have to tell Python what type of empty container you want it to create when it finds a brand new row.


        # If we used a List []: A list is like a stack of papers. If the computer wants to know if seat 4 is in the list, it has to check the first paper... then the second paper... then the third... until it finds it. If the list is long, this takes time.

        # If we use a Set {}: A Set is like a VIP bouncer at a club. You don't have to search the whole club. You just ask the bouncer, "Is number 4 inside?" and the bouncer instantly says "Yes" or "No".

        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                seat_taken_by_row[row].add(seat)

        for row, taken_seats in seat_taken_by_row.items():
            total_families -= 2
            
            left_free = 2 not in taken_seats and 3 not in taken_seats and 4 not in taken_seats and 5 not in taken_seats
            right_free = 6 not in taken_seats and 7 not in taken_seats and 8 not in taken_seats and 9 not in taken_seats
            middle_free = 4 not in taken_seats and 5 not in taken_seats and 6 not in taken_seats and 7 not in taken_seats

            # Add back whatever we can fit
            if left_free and right_free:
                total_families += 2
            elif left_free or right_free or middle_free:
                total_families += 1
                
        # We did it!
        return total_families