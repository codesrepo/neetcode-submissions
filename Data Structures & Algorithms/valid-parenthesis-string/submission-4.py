class Solution:
    def checkValidString(self, s: str) -> bool:
        # Think of every '*' as a three-way fork: it can become '(', ')' or "".
        # A string with k stars therefore has 3^k possible "castings".
        # Instead of exploring them one by one, track ALL of them at once with
        # just two numbers:
        #
        #   After reading any prefix of s, ask: "across every casting of the
        #   stars seen so far, how many '(' could currently be open (unclosed)?"
        #
        #   lo = the SMALLEST possible open count  (stars pessimistically
        #        cast as ')' or "" — closing as much as possible)
        #   hi = the LARGEST possible open count   (stars optimistically
        #        cast as '(' — opening as much as possible)
        #
        # The achievable open counts always form the contiguous range
        # [lo, hi]: each '*' nudges a count by +1, -1 or 0, so no gaps appear.
        # That's why two endpoints are enough to represent 3^k branches.
        #
        # O(n) time, O(1) space.
        lo = hi = 0
        for ch in s:
            if ch == '(':
                # A real '(' opens one more paren in EVERY casting:
                # the whole range shifts up by 1.
                lo += 1; hi += 1
            elif ch == ')':
                # A real ')' closes one paren in every casting:
                # the whole range shifts down by 1.
                hi -= 1
                if hi < 0:
                    # Even the most optimistic casting (every star was '(')
                    # has more ')' than '(' in this prefix -> no casting can
                    # survive -> invalid, stop early.
                    return False
                if lo: lo -= 1
                # ^ lo is clamped at 0 (this is max(lo - 1, 0)). A casting
                # whose open count would go below 0 just died: this ')' had
                # nothing to close in it. We silently drop those dead
                # branches; the surviving minimum is 0.
            else:  # ch == '*'
                # The wildcard fans out: as '(' it pushes the max up,
                # as ')' (or "") it pulls the min down.
                hi += 1
                if lo: lo -= 1
                # ^ same clamp: if lo is already 0, the star's best "minimal"
                # role is the empty string "", not ')' (which would kill the
                # branch), so the minimum stays 0.
        # Valid  <=>  some casting ends with every '(' closed
        #        <=>  0 is inside the final range [lo, hi].
        # hi >= 0 is guaranteed (we returned early otherwise), so we only
        # need to check the bottom end:
        return lo == 0

        # Worked trace for s = "((**)":
        #   ch   lo  hi   range of possible open counts
        #   (     1   1   {1}
        #   (     2   2   {2}
        #   *     1   3   {1,2,3}   star as ')' / "" / '('
        #   *     0   4   {0..4}
        #   )     0   3   {0..3}    lo clamped: dead branches dropped
        #   end: lo == 0 -> True    (e.g. star1="", star2=')' gives "(())")
        #
        # Worked trace for s = "(((*)":
        #   (  1 1 | (  2 2 | (  3 3 | *  2 4 | )  1 3
        #   end: lo == 1 -> False   (at least one '(' unclosed in every casting)
