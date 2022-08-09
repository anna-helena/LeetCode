class SnapshotArray:

    def __init__(self, length: int):
        self.vals = {}
        self.time_vals = {}
        self.snaps = -1

    def set(self, index: int, val: int) -> None:
        self.vals[index] = val

    def snap(self) -> int:
        self.snaps += 1
        self.time_vals[self.snaps] = self.vals.copy()
        return self.snaps 

    def get(self, index: int, snap_id: int) -> int:
        vals = self.time_vals[snap_id]
        if index in vals:
            return vals[index]
        else:
            return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)