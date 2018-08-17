class Solution:

    def to_english(self, n):

        num_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                      27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                      50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
                      73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95,
                      96, 97, 98, 99]

        num_english = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
                       'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen',
                       'Twenty', 'Twenty One', 'Twenty Two', 'Twenty Three', 'Twenty Four', 'Twenty Five',
                       'Twenty Six', 'Twenty Seven', 'Twenty Eight', 'Twenty Nine', 'Thirty', 'Thirty One',
                       'Thirty Two', 'Thirty Three', 'Thirty Four', 'Thirty Five', 'Thirty Six', 'Thirty Seven',
                       'Thirty Eight', 'Thirty Nine', 'Forty', 'Forty One', 'Forty Two', 'Forty Three',
                       'Forty Four', 'Forty Five', 'Forty Six', 'Forty Seven', 'Forty Eight', 'Forty Nine', 'Fifty',
                       'Fifty One', 'Fifty Two', 'Fifty Three', 'Fifty Four', 'Fifty Five', 'Fifty Six',
                       'Fifty Seven', 'Fifty Eight', 'Fifty Nine', 'Sixty', 'Sixty One', 'Sixty Two', 'Sixty Three',
                       'Sixty Four', 'Sixty Five', 'Sixty Six', 'Sixty Seven', 'Sixty Eight', 'Sixty Nine',
                       'Seventy', 'Seventy One', 'Seventy Two', 'Seventy Three', 'Seventy Four', 'Seventy Five',
                       'Seventy Six', 'Seventy Seven', 'Seventy Eight', 'Seventy Nine', 'Eighty', 'Eighty One',
                       'Eighty Two', 'Eighty Three', 'Eighty Four', 'Eighty Five', 'Eighty Six', 'Eighty Seven',
                       'Eighty Eight', 'Eighty Nine', 'Ninety', 'Ninety One', 'Ninety Two', 'Ninety Three',
                       'Ninety Four', 'Ninety Five', 'Ninety Six', 'Ninety Seven', 'Ninety Eight', 'Ninety Nine']

        number_table = dict(zip(num_digits, num_english))

        if n == 0:
            return ""

        english_string = number_table[n % 100]

        if n >= 100:
            english_string = number_table[int((n / 100))] + ' Hundred ' + english_string

        return english_string.strip()

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return "Zero"

        num_scale = dict()
        num_english = dict()

        num_scale['hundred'] = int(num % 1000)
        num_scale['thousand'] = int(num / pow(1000, 1) % 1000)
        num_scale['million'] = int(num / pow(1000, 2) % 1000)
        num_scale['billion'] = int(num / pow(1000, 3) % 1000)

        for k, v in num_scale.items():
            num_english[k] = self.to_english(v)

        english_string = ''
        if num >= 1 and num_english['hundred'] != '':
            english_string = " ".join( [ num_english['hundred'], english_string ])
        if num >= 1000 and num_english['thousand'] != '':
            english_string = " ".join( [ num_english['thousand'], 'Thousand', english_string])
        if num >= 1000000 and num_english['million'] != '':
            english_string = " ".join( [ num_english['million'], 'Million', english_string ] )
        if num >= 1 and num_english['billion'] != '':
            english_string = " ".join( [ num_english['billion'], 'Billion', english_string ] )

        return english_string.strip()
        # return (num_scale, num_english)


if __name__ == '__main__':
    num = 100
    s = Solution().numberToWords(num)

    from pprint import pprint

    pprint(s)
