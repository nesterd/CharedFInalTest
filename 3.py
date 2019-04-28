from PIL import ImageDraw


class ImageDrawer(ImageDraw.ImageDraw):
    @staticmethod
    def get_points(xy, height):
        return [(xy[0], xy[1]), (xy[0], xy[1] + height), (xy[2], xy[3]), (xy[2], xy[3] - height)]

    @staticmethod
    def get_points_up(xy, height):
        return [(xy[0], xy[3]), (xy[2], xy[1] + height), (xy[2], xy[1]), (xy[0], xy[3] - height)]

    def down_parallelogram(self, xy, height, fill=None, outline=None):
        points = self.get_points(xy, height)
        self.polygon(points, fill, outline)

    def up_parallelogram(self, xy, height, fill=None, outline=None):
        points = self.get_points_up(xy, height)
        self.polygon(points, fill, outline)







