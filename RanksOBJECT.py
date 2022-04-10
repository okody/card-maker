# A class Hold Ranks Cards
from PIL import Image, ImageDraw, ImageFont




# A class hold the information of the staff info
class Staff_Info:
    def __init__(self,ID,Staff_Name,Staff_Rank,Instgram,Telegram,Steam):
        self.ID = ID
        self.Staff_Name = Staff_Name
        self.Staff_Rank = Staff_Rank
        self.Instgram_Account = Instgram
        self.Telegram_Account = Telegram
        self.Steam_Account = Steam


class Ranks(Staff_Info):
    def __init__(self,ID,Staff_Name,Staff_Rank,Instgram,Telegram, Steam):
        Staff_Info.__init__(self,ID,Staff_Name,Staff_Rank,Instgram,Telegram,Steam)
        self.Founder = Image.open('StaffCardPrototype/Founder.png')
        self.HeadAdmin = Image.open('StaffCardPrototype/HeadAdmin.png')
        self.SuperAdmin = Image.open('StaffCardPrototype/SuperAdmin.png')
        self.Admin = Image.open('StaffCardPrototype/Admin.png')
        self.ACT = Image.open('StaffCardPrototype/ACT.png')
        self.TelegramLogo = Image.open('AccountsLogoes/TelegramLogo.png')
        self.SteamLogo = Image.open('AccountsLogoes/SteamLogo.png')
        self.InstgramLogo = Image.open('AccountsLogoes/InstgramLogo.png')
        self.AccountUp = (22, 418)
        self.AccountDown = (22, 455)
        self.NY = 340
        self.Cardsize = 150, 244

        # Width and Height of the Cards
        self.Card_Width, self.Card_Height = self.Founder.size

        # Name Font Type how to objectify it by using ImageFont
        self.Name_Font_Type = ImageFont.truetype('CardFonts/NameFont.ttf', 30)
        self.Accounts_Font_Type = ImageFont.truetype('CardFonts/AccountFont.ttf', 20)

        # Width and Height of the Staff Name Size

        self.Name_Width, self.Name_Height = self.Name_Font_Type.getsize(self.Staff_Name)



    def Accounts(self,DrawCard):

        UAX = 420
        DAX = 456

        if self.Steam_Account != None and self.Instgram_Account != None and self.Telegram_Account != None:
            DrawCard.text((54,UAX),self.Telegram_Account, font= self.Accounts_Font_Type)
            DrawCard.text((54, DAX), self.Steam_Account, font= self.Accounts_Font_Type)



        elif self.Instgram_Account != None and self.Telegram_Account != None:
            DrawCard.text((54,UAX),self.Telegram_Account, font= self.Accounts_Font_Type)

        elif self.Steam_Account != None and self.Instgram_Account != None:
            DrawCard.text((54,UAX),self.Instgram_Account, font= self.Accounts_Font_Type)
            DrawCard.text((54, DAX), self.Steam_Account, font= self.Accounts_Font_Type)

        elif self.Steam_Account != None and self.Telegram_Account != None:
            DrawCard.text((54,UAX),self.Telegram_Account, font= self.Accounts_Font_Type)
            DrawCard.text((54, DAX), self.Steam_Account, font= self.Accounts_Font_Type)

        elif self.Telegram_Account != None:
            DrawCard.text((54,UAX),self.Telegram_Account, font= self.Accounts_Font_Type)

        elif self.Steam_Account != None:
            DrawCard.text((54, DAX), self.Steam_Account, font= self.Accounts_Font_Type)

        elif self.Instgram_Account != None:
            DrawCard.text((54, UAX), self.Instgram_Account, font=self.Accounts_Font_Type)

        return DrawCard


    def AccountsLogo(self,Card):

        if self.Steam_Account != None and self.Instgram_Account != None and self.Telegram_Account != None:
            Card.alpha_composite(self.TelegramLogo, self.AccountUp)
            Card.alpha_composite(self.SteamLogo, self.AccountDown)

        elif self.Instgram_Account != None and self.Telegram_Account != None:
            Card.alpha_composite(self.TelegramLogo, self.AccountUp)


        elif self.Steam_Account != None and self.Instgram_Account != None:
            Card.alpha_composite(self.InstgramLogo, self.AccountUp)
            Card.alpha_composite(self.SteamLogo, self.AccountDown)

        elif self.Steam_Account != None and self.Telegram_Account != None:
            Card.alpha_composite(self.TelegramLogo, self.AccountUp)
            Card.alpha_composite(self.SteamLogo, self.AccountDown)

        elif self.Steam_Account != None:
            Card.alpha_composite(self.SteamLogo, self.AccountDown)


        elif self.Telegram_Account != None:
            Card.alpha_composite(self.TelegramLogo, self.AccountUp)


        elif self.Instgram_Account != None:
            Card.alpha_composite(self.InstgramLogo, self.AccountUp)


        return Card



    def FounderF(self):

        CardDraw_BA = ImageDraw.Draw(self.Founder)
        CardDraw_AA = self.Accounts(CardDraw_BA)
        self.Founder = self.AccountsLogo(self.Founder)

        CardDraw_AA.text(((self.Card_Width- self.Name_Width) / 2, self.NY), self.Staff_Name, fill=(50, 50, 50),font=self.Name_Font_Type)

        self.Founder.thumbnail(self.Cardsize)
        self.Founder.save('StaffCards/{}.png'.format(self.Staff_Name.upper()+"_FOUNDER"))

    def HeadAdminF(self):

        CardDraw_BA = ImageDraw.Draw(self.HeadAdmin)
        CardDraw_AA = self.Accounts(CardDraw_BA)
        self.HeadAdmin = self.AccountsLogo(self.HeadAdmin)

        CardDraw_AA.text(((self.Card_Width- self.Name_Width) / 2, self.NY), self.Staff_Name, fill=(50, 50, 50),
                         font=self.Name_Font_Type)

        self.HeadAdmin.thumbnail(self.Cardsize)
        self.HeadAdmin.save('StaffCards/{}.png'.format(self.Staff_Name.upper()+"_HEADADMIN"))

    def SuperAdminF(self):

        CardDraw_BA = ImageDraw.Draw(self.SuperAdmin)
        CardDraw_AA = self.Accounts(CardDraw_BA)
        self.SuperAdmin = self.AccountsLogo(self.SuperAdmin)

        CardDraw_AA.text(((self.Card_Width- self.Name_Width) / 2, self.NY), self.Staff_Name, fill=(50, 50, 50),
                      font=self.Name_Font_Type)

        self.SuperAdmin.thumbnail(self.Cardsize)
        self.SuperAdmin.save('StaffCards/{}.png'.format(self.Staff_Name.upper()+"_SUPERADMIN"))

    def AdminF(self):

        CardDraw_BA = ImageDraw.Draw(self.Admin)
        CardDraw_AA = self.Accounts(CardDraw_BA)
        self.Admin = self.AccountsLogo(self.Admin)

        CardDraw_AA.text(((self.Card_Width- self.Name_Width) / 2, self.NY), self.Staff_Name, fill=(50, 50, 50),
                         font=self.Name_Font_Type)

        self.Admin.thumbnail(self.Cardsize)
        self.Admin.save('StaffCards/{}.png'.format(self.Staff_Name.upper()+"_ADMIN"))

    def ACTF(self):

        CardDraw_BA = ImageDraw.Draw(self.ACT)
        CardDraw_AA = self.Accounts(CardDraw_BA)
        self.ACT = self.AccountsLogo(self.ACT)

        CardDraw_AA.text(( (self.Card_Width- self.Name_Width) / 2, self.NY), self.Staff_Name, fill=(50, 50, 50),
                         font=self.Name_Font_Type)

        self.ACT.thumbnail(self.Cardsize)
        self.ACT.save('StaffCards/{}.png'.format(self.Staff_Name.upper()+"_ACT"))