class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Guard clauses: if s is shorter than t, no valid window can exist.
        if not s or not t or len(s) < len(t):
            return ""

        # Build a frequency map of characters we still NEED from t.
        # Example: t = "ABC"  -> required = {'A': 1, 'B': 1, 'C': 1}
        #          t = "AABC" -> required = {'A': 2, 'B': 1, 'C': 1}
        # As we consume chars from s, we decrement these counts. A negative
        # count means the window has *extra* copies of that char beyond what's
        # required (still valid, just not minimal yet).
        required = {}
        for c in t:
            required[c] = required.get(c, 0) + 1

        # `missing` = how many characters (counting duplicates) we still need
        # to see before the window becomes valid. Starts at len(t); reaches 0
        # exactly when the window covers all of t.
        missing = len(t)

        # Sliding window pointers and best-answer tracker.
        left = 0
        best_l, best_r = 0, -1            # -1 sentinel: "no valid window yet"
        best_len = len(s) + 1             # any real window will be smaller

        # ---- Expand phase: walk `right` across s one char at a time ----
        for right, c in enumerate(s):
            # If c is a character we care about, account for it.
            if c in required:
                # Only chars we still NEED (count > 0) reduce `missing`.
                # If count is already <= 0, we have a surplus; adding another
                # doesn't make the window "more valid".
                if required[c] > 0:
                    missing -= 1
                # Either way, decrement: surplus is tracked as negative count,
                # which is what lets us safely shrink past extra copies later.
                required[c] -= 1

            # ---- Shrink phase: while window is valid, pull `left` in ----
            # Each shrink either improves our answer or proves it can't be
            # improved further without breaking validity.
            while missing == 0:
                # Record this window if it's the shortest valid one so far.
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_l, best_r = left, right

                # Try to drop s[left] from the window.
                left_c = s[left]
                if left_c in required:
                    # Putting the char back into "required" budget.
                    required[left_c] += 1
                    # If the count goes positive, the window is now short
                    # one copy of left_c — no longer valid. Bump `missing`
                    # so the while-loop exits and `right` can advance.
                    if required[left_c] > 0:
                        missing += 1
                left += 1

        # If best_r was never updated past its -1 sentinel, no window exists.
        return s[best_l:best_r + 1] if best_r >= best_l else ""



                



        