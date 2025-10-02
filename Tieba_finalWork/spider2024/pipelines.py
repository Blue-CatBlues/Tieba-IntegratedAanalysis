import openpyxl

class ExcelPipeline:
    def open_spider(self, spider):
        # 当爬虫开启时调用此方法，创建一个新的 Excel 工作簿
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.append(['贴吧', '关注人数', '帖子数', '简介', '类型'])
        spider.logger.info("Excel 文件已创建")

    def close_spider(self, spider):
        self.wb.save('Tieba_output.xlsx')
        spider.logger.info("Excel 文件已保存")

    def process_item(self, item, spider):
        spider.logger.info(f"处理项目: {item['name']}, {item['member']}, {item['comment']}, {item['main']}, {item['type']}")
        self.sheet.append([item['name'], item['member'], item['comment'], item['main'], item['type']])
        return item