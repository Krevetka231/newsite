from flask import Flask, render_template, url_for,request,redirect 
from flask_sqlalchemy import SQLAlchemy 
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db' #с какой базой данных он работает. Обязательно писать все что до знака "равно"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # чтобы отключить предупреждения
db = SQLAlchemy(app)




@app.route('/',methods=['POST','GET'])
@app.route('/main',methods=['POST','GET'])
def main_page():
 if request.method == 'POST': 
     return redirect('/')
 else:
    items = {
    '6': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIh9RZIfmPFCMhx7n7KsGQIbQaDNhTZ272Hw&s', #cатаник
    '7': 'https://www.meme-arsenal.com/memes/ebcab9718dbe08035915d7989ec11bdd.jpg', #алебарда
    '8': 'https://courier.spectral.gg/images/dota/profile_badges/spirit_vessel.png?size=!source&2', #весля
    '9': 'https://images.steamusercontent.com/ugc/535137537453259179/55EF08C278345A865E74A769B9E459E73285E391/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false',#армлет
    '1': 'https://www.gamersdecide.com/sites/default/files/styles/image_auto_x_auto/public/authors/u172764/boots_of_bearing.webp?itok=DfcoqJ12', #барабано тапки
    '2': 'https://dota2ok.ru/wp-content/uploads/2017/09/phase_boots_lg200.png',# фазы
    '3': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQC16H5kN4Kj7R416tUGdtvpJblQ_y4LNjoYw&s',#пт
    '4': 'https://dota2ok.ru/wp-content/cache/thumb/f79a3f318_320x200.jpg',#грейвсы
    '5': 'https://dota2ok.ru/wp-content/cache/thumb/c89fb5ab3_320x200.png',#тревела
    '10': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSI18U8BajUFVSUVrddSVKZ5L9g0f12nHR03g&s', #rapier
    '11': 'https://dota2ok.ru/wp-content/cache/thumb/ab23fdeb2_320x200.png',#bm
    '12': 'https://dota2ok.ru/wp-content/cache/thumb/e8017423f_320x200.jpg',#skadi
    '13': 'https://media.discordapp.net/attachments/1363927523775484064/1384514506591309915/image.png?ex=6852b51d&is=6851639d&hm=12e3a0727af66922edfb898499dbceefcbf8f36bbc60fe2e1d6267122295c702&=&format=webp&quality=lossless',#ветра
    '14':'https://media.discordapp.net/attachments/1363927523775484064/1384618726917279904/image.png?ex=6853162d&is=6851c4ad&hm=647f7629e9ad707154f0a52fb0eecc12cd8e0a84a4c2af3fd13caf19e53dfbf7&=&format=webp&quality=lossless',#домик
    '15':'https://media.discordapp.net/attachments/1363927523775484064/1384619456172654853/image.png?ex=685316db&is=6851c55b&hm=34ae58d8f0c2ed66d27598a89f3e762bc84726c9a59f6d8ee027413f033639fe&=&format=webp&quality=lossless',#midas
    '16':'https://cdn.discordapp.com/attachments/1363927523775484064/1384619554155794582/image.png?ex=685316f2&is=6851c572&hm=e28389a23fdcf8737682176df5560681d5b6bf7a4a84a599d3d36e7b0c970818&',#moonshard
    '17':'https://media.discordapp.net/attachments/1363927523775484064/1384619835513901107/image.png?ex=68531735&is=6851c5b5&hm=d4995871b654284ab942ee3e31edfed96e4b3d8687ae0e6fb00561dae608b99b&=&format=webp&quality=lossless',#mom
    '18':'https://cdn.discordapp.com/attachments/1363927523775484064/1384620299521228991/image.png?ex=685317a4&is=6851c624&hm=7828ad7fb142706a2875ab5b5f336b4455e2d248fa864fc71ff5048b3b1ff81e&',#domik apnuytiu
    '19':'https://media.discordapp.net/attachments/1363927523775484064/1384620570422808588/image.png?ex=685317e4&is=6851c664&hm=d26b4e36100f178c891af63315ff30eebb367b710135166c0777ed2926398d0f&=&format=webp&quality=lossless',#pipe
    '20':'https://media.discordapp.net/attachments/1363927523775484064/1384620751637844199/image.png?ex=68531810&is=6851c690&hm=f143f3d6ea2d338d569fd57afc7188088ef38ef22dbafa1b62bb75669086d441&=&format=webp&quality=lossless',#parsma
    '21':'https://media.discordapp.net/attachments/1363927523775484064/1384622064773627964/image.png?ex=68531949&is=6851c7c9&hm=2d87f9a0849aa216917b161e498c6e59949782ffc7dcd6c97c180d4a450fe626&=&format=webp&quality=lossless',
    '22':'https://media.discordapp.net/attachments/1363927523775484064/1384622092963811418/image.png?ex=6853194f&is=6851c7cf&hm=bed0a238aa37979d8daa773dc62d411b24973f52f2873da383584cb5b3576945&=&format=webp&quality=lossless',
    '23':'https://media.discordapp.net/attachments/1363927523775484064/1384622118158864384/image.png?ex=68531956&is=6851c7d6&hm=18d84dd26ecc936d707d5d82214e3d3c2ce06effe8310de3705e784d05509ed6&=&format=webp&quality=lossless',
    '24':'https://media.discordapp.net/attachments/1363927523775484064/1384622135993176236/image.png?ex=6853195a&is=6851c7da&hm=c4e364b3269efe9e05c9ab67629dde7d140428e5db3a36a4316bb6f5d42a1294&=&format=webp&quality=lossless',
    '25':'https://media.discordapp.net/attachments/1363927523775484064/1384622153038565416/image.png?ex=6853195e&is=6851c7de&hm=50b87f495112954ecd8992f2afc80dac7d6e17ec12d93a8f5ec90cfe81b1d869&=&format=webp&quality=lossless',
    '26':'https://media.discordapp.net/attachments/1363927523775484064/1384622167307714680/image.png?ex=68531961&is=6851c7e1&hm=f0273eb3a3f28e6e6118e45c8f3da0ffc12691071c99b1708738d8775d704d2e&=&format=webp&quality=lossless',
    '27':'https://media.discordapp.net/attachments/1363927523775484064/1384622187025268756/image.png?ex=68531966&is=6851c7e6&hm=acfb8b17d86ced4bfa94494d4abad3aba223bcf130c54a2b5bbe04bc9fc28e37&=&format=webp&quality=lossless',
    '28':'https://media.discordapp.net/attachments/1363927523775484064/1384622205329215629/image.png?ex=6853196a&is=6851c7ea&hm=150c2eca9e79b0ab49e9401c2fdc82517bbf280ac163c963bfb13a584337a7ba&=&format=webp&quality=lossless',
    '29':'https://media.discordapp.net/attachments/1363927523775484064/1384622230281125928/image.png?ex=68531970&is=6851c7f0&hm=aff88e582f7ab98decffd59cf38671ecf8a8cf0fc6d14d510fdf0433b0aefc77&=&format=webp&quality=lossless',
    '30':'https://media.discordapp.net/attachments/1363927523775484064/1384622245292281987/image.png?ex=68531974&is=6851c7f4&hm=5645f8e2673e494fa191b66e483294f5f62c22130ee5b8a7c067cc2ba296ba25&=&format=webp&quality=lossless',
    '31':'https://media.discordapp.net/attachments/1363927523775484064/1384622261817835681/image.png?ex=68531978&is=6851c7f8&hm=e66cd732734343fd8b84b0b8ea0371b6969cc7e5b8340e9409bcfd15fc0db215&=&format=webp&quality=lossless',
    '32':'https://media.discordapp.net/attachments/1363927523775484064/1384622316222288034/image.png?ex=68531985&is=6851c805&hm=e987960faf7705f3c9b9a4c5ad1680fda272547040a153a60e1bfa33e41684b1&=&format=webp&quality=lossless',
    '33':'https://media.discordapp.net/attachments/1363927523775484064/1384622334165516320/image.png?ex=68531989&is=6851c809&hm=5d71300ee5468995ca66ebc7b20012dfe59ab9d7d4480598120ffcf4b0af1718&=&format=webp&quality=lossless',
    '34':'https://media.discordapp.net/attachments/1363927523775484064/1384622362338525415/image.png?ex=68531990&is=6851c810&hm=1bf9ae5bdc8cdc98fc82c7233fe5a488fdf6aac2f91f21d610924075560a8314&=&format=webp&quality=lossless',
    '35':'https://media.discordapp.net/attachments/1363927523775484064/1384622384979382432/image.png?ex=68531995&is=6851c815&hm=a682dec6d903b6642de6a50715c82927915ff03153427f09f73166ec1f738803&=&format=webp&quality=lossless',
    '36':'https://media.discordapp.net/attachments/1363927523775484064/1384622398678241470/image.png?ex=68531998&is=6851c818&hm=fb6fc52c1b6d840254602c25e69d6460819f3d3922329cd2a3a7b52acdd8d136&=&format=webp&quality=lossless',
    '37':'https://media.discordapp.net/attachments/1363927523775484064/1384622416873127937/image.png?ex=6853199d&is=6851c81d&hm=4934708f92c81a1aa8d53642162d3d52cdd75e8e3bd4bb45238a0b5725f4608f&=&format=webp&quality=lossless',
    '38':'https://media.discordapp.net/attachments/1363927523775484064/1384622436565258321/image.png?ex=685319a1&is=6851c821&hm=20350773478c0b634a6feb55dea242661394e4f9fef436d22ad43acb75c17bab&=&format=webp&quality=lossless',
    '39':'https://media.discordapp.net/attachments/1363927523775484064/1384622457893159044/image.png?ex=685319a7&is=6851c827&hm=ef8a7b5933d7efe58570ff758ad4df9d4680422bf9199b0f405ad9efebe68639&=&format=webp&quality=lossless',
    '40':'https://media.discordapp.net/attachments/1363927523775484064/1384622496007061545/image.png?ex=685319b0&is=6851c830&hm=b19bae3ba35d01967622d6ccd39124a5e4ac2b49f8f2f1a1fe956820ba8f63ea&=&format=webp&quality=lossless',
    '41':'https://media.discordapp.net/attachments/1363927523775484064/1384622511924449382/image.png?ex=685319b3&is=6851c833&hm=f65f036fd509c91c422531de7275909a15cddde441691a36953067217efd612f&=&format=webp&quality=lossless',
    '42':'https://media.discordapp.net/attachments/1363927523775484064/1384622539262787604/image.png?ex=685319ba&is=6851c83a&hm=b94517eacb10c3f70365ef9cbcf124b598a0b75eab1cfa581b599ec3f4924563&=&format=webp&quality=lossless',
    '43':'https://media.discordapp.net/attachments/1363927523775484064/1384622555369050284/image.png?ex=685319be&is=6851c83e&hm=48434f7fe3667bd3eeaedce959246f08adb129bf52abe397a80023bd54d0f599&=&format=webp&quality=lossless',
    '44':'https://media.discordapp.net/attachments/1363927523775484064/1384622590479569039/image.png?ex=685319c6&is=6851c846&hm=7a75fd291774e0d537108131313f3e7bace884fda9310b60776e19915470a8f5&=&format=webp&quality=lossless',
    '45':'https://media.discordapp.net/attachments/1363927523775484064/1384622609861447841/image.png?ex=685319cb&is=6851c84b&hm=a95cf24b19b96d659972359ce69bd97415151d235a072b029d9e89d554426b46&=&format=webp&quality=lossless',
    '46':'https://media.discordapp.net/attachments/1363927523775484064/1384622710046326965/image.png?ex=685319e3&is=6851c863&hm=90a1e284bb7030a8c92cdcf8eefb954d42c38995adcd862dee537d141d269ad1&=&format=webp&quality=lossless',
    '47':'https://media.discordapp.net/attachments/1363927523775484064/1384622732104433744/image.png?ex=685319e8&is=6851c868&hm=caa611e4fe24c2d2cf2cc0eb9cd762e9c264eb6cda41f3901acfc22346ebafe1&=&format=webp&quality=lossless',
    '48':'https://media.discordapp.net/attachments/1363927523775484064/1384622753310838814/image.png?ex=685319ed&is=6851c86d&hm=28275f9a53b964d7f6c01c0b51b93e9d4e75668152a3790f96e870a8c25b8c1a&=&format=webp&quality=lossless',
    '49':'https://media.discordapp.net/attachments/1363927523775484064/1384622773174927490/image.png?ex=685319f2&is=6851c872&hm=dc21bb56aada741ffb242935b5c62f1a7fbdc6d97ffee2629725881d6aeb3b19&=&format=webp&quality=lossless',
    '50':'https://media.discordapp.net/attachments/1363927523775484064/1384622794733785290/image.png?ex=685319f7&is=6851c877&hm=18a2d065f35375fe82c534db708d5a37a6feb7d452864e7fdbcb0c4048d42b3e&=&format=webp&quality=lossless',
    '51':'https://media.discordapp.net/attachments/1363927523775484064/1384623022551470281/image.png?ex=68531a2d&is=6851c8ad&hm=068551949d72033510dff4342011f21c27cad81983ee3443c2b765939f21fea4&=&format=webp&quality=lossless',
    '52':'https://media.discordapp.net/attachments/1363927523775484064/1384623038263332924/image.png?ex=68531a31&is=6851c8b1&hm=a75bd9e4a1122e4ef3ff8cbd6fa5bf3a527153121875f518f4cfca3b8c8949d7&=&format=webp&quality=lossless',
    '53':'https://media.discordapp.net/attachments/1363927523775484064/1384623055355252910/image.png?ex=68531a35&is=6851c8b5&hm=26916b61696559bcb099dd3379b5ae8e5964e37b8b2307c569142ef43beed989&=&format=webp&quality=lossless',
    '54':'https://media.discordapp.net/attachments/1363927523775484064/1384623115249651923/image.png?ex=68531a43&is=6851c8c3&hm=24596bde4982287d3740d94f7ac86ec8e52c8e514f5bf36091b4ed6a3dd85fbb&=&format=webp&quality=lossless',
    '55':'https://media.discordapp.net/attachments/1363927523775484064/1384623141858443404/image.png?ex=68531a4a&is=6851c8ca&hm=2428b3212e02960c6c6d5c43d68069e28558b68f99235e160657aed4284eea0e&=&format=webp&quality=lossless',
    '56':'https://media.discordapp.net/attachments/1363927523775484064/1384623159273324574/image.png?ex=68531a4e&is=6851c8ce&hm=9791d0e1e1f2317bcffac9380ec9a3752cf422a90f861c321a96ed9802076d97&=&format=webp&quality=lossless',
    '57':'https://media.discordapp.net/attachments/1363927523775484064/1384623176079642805/image.png?ex=68531a52&is=6851c8d2&hm=f14d10d08e61eb8851ceff8c0ad0292b87700fb6a04364ae8308d910fb071d1e&=&format=webp&quality=lossless',
    '58':'https://media.discordapp.net/attachments/1363927523775484064/1384623189270986833/image.png?ex=68531a55&is=6851c8d5&hm=400b34c8d98979bcf84640cc0af4f3f86738f2019a4f9e8cf274f58f20476e39&=&format=webp&quality=lossless',
    '59':'https://media.discordapp.net/attachments/1363927523775484064/1384623233688404060/image.png?ex=68531a5f&is=6851c8df&hm=0cc7ed0734b1dd319eeccfaf9dcc03b12657aebc3f1b7e7c30ea5cc3b0633039&=&format=webp&quality=lossless',
    '60':'https://media.discordapp.net/attachments/1363927523775484064/1384623247886389298/image.png?ex=68531a63&is=6851c8e3&hm=ae2293a7107ad067ebb01e784c907b7a0c8eb2d0078e0defa3326d987e2c74e0&=&format=webp&quality=lossless',
    '61':'https://media.discordapp.net/attachments/1363927523775484064/1384623275430379643/image.png?ex=68531a69&is=6851c8e9&hm=4ef201c25741be3aca7642c187ac03520676c04613fb8179a1c939403e125ceb&=&format=webp&quality=lossless',
    '62':'https://media.discordapp.net/attachments/1363927523775484064/1384623291754479737/image.png?ex=68531a6d&is=6851c8ed&hm=4d5a1deae7beecb10826592652d97fe14b0884ed3a092e0950713e167b72896f&=&format=webp&quality=lossless',
    '63':'https://media.discordapp.net/attachments/1363927523775484064/1384626509939081236/asdjaksdj.png?ex=68531d6d&is=6851cbed&hm=1f1e4b48a49ad438a005d652fb816c13374014b7c36ff3a30baa2962bd108e43&=&format=webp&quality=lossless',
    '64':'https://media.discordapp.net/attachments/1363927523775484064/1384626509939081236/asdjaksdj.png?ex=68531d6d&is=6851cbed&hm=1f1e4b48a49ad438a005d652fb816c13374014b7c36ff3a30baa2962bd108e43&=&format=webp&quality=lossless',
    '65':'https://media.discordapp.net/attachments/1363927523775484064/1384626509939081236/asdjaksdj.png?ex=68531d6d&is=6851cbed&hm=1f1e4b48a49ad438a005d652fb816c13374014b7c36ff3a30baa2962bd108e43&=&format=webp&quality=lossless',
    '66':'https://media.discordapp.net/attachments/1363927523775484064/1384626509939081236/asdjaksdj.png?ex=68531d6d&is=6851cbed&hm=1f1e4b48a49ad438a005d652fb816c13374014b7c36ff3a30baa2962bd108e43&=&format=webp&quality=lossless',
    '67':'https://media.discordapp.net/attachments/1363927523775484064/1384626509939081236/asdjaksdj.png?ex=68531d6d&is=6851cbed&hm=1f1e4b48a49ad438a005d652fb816c13374014b7c36ff3a30baa2962bd108e43&=&format=webp&quality=lossless',     
    }
    item1 = str(random.randint(1, 5))
    item2 = str(random.randint(6, len(items)))
    item3 = str(random.randint(6, len(items)))
    item4 = str(random.randint(6, len(items)))
    item5 = str(random.randint(6, len(items)))
    item6 = str(random.randint(6, len(items)))
    position = random.randint(1,5)
    return render_template('main_page.html',items = items,item1 = item1,item2 = item2,item3 = item3,item4 = item4,item5 = item5,item6 = item6,position = position)





if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)  









