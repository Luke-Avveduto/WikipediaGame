import wikipediaapi

class PageNode:

    def __init__(self, page: wikipediaapi.WikipediaPage) -> None:
        self.page = page


    def get_connected_nodes(self) -> list[PageNode]:
        """Creates returns of a list of all the pages linked to by this page, wrapped in PageNode objects"""
        output = []

        for key in self.page.links.keys():
            output.append(PageNode(self.page.links[key]))
        
        return output