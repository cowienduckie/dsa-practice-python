from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # The root folders are the folders that always have the shortest depth in its tree
        # So, we ascending sort folders by depth
        def get_depth(path: str) -> int:
            return len(path.split("/"))

        folder.sort(key=lambda path: get_depth(path))

        # Use set to store root folders
        # And loop through all possible parent folders of each folder, to check if it has any parent
        # If not, add it to answer set
        root_set = set()
        for path in folder:
            sub_folders = path.split("/")
            parent = ""

            for i in range(1, len(sub_folders)):
                if parent in root_set:
                    break
                parent = parent + "/" + sub_folders[i]

            if parent == path:
                root_set.add(path)

        return list(root_set)


print(Solution().removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
