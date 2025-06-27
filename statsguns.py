def stats(response,idarma):

    lista_stats=[]
    lista_nome_stats=[]

    stats=response['data'][idarma]['weaponStats']
    try:
        adsStats=stats['adsStats']
    except:
        pass
    damageranges=stats['damageRanges']

    fireRate=stats['fireRate']
    lista_stats.append(fireRate)
    lista_nome_stats.append('fire Rate')

    magazineSize=stats['magazineSize']
    lista_stats.append(magazineSize)
    lista_nome_stats.append('magazine Size')

    runSpeedMultiplier=stats['runSpeedMultiplier']*6.75
    lista_stats.append(runSpeedMultiplier)
    lista_nome_stats.append('runSpeed Multiplier')

    equipTimeSeconds=stats['equipTimeSeconds']              #general stats
    lista_stats.append(equipTimeSeconds)
    lista_nome_stats.append('equip Time Seconds')

    reloadTimeSeconds=stats['reloadTimeSeconds']
    lista_stats.append(reloadTimeSeconds)
    lista_nome_stats.append('reload Time Seconds')

    firstBulletAccuracy=stats['firstBulletAccuracy']
    lista_stats.append(firstBulletAccuracy)
    lista_nome_stats.append('equip Time Seconds')

    try:
        zoomMultiplierads=adsStats['zoomMultiplier']
        lista_stats.append(zoomMultiplierads)
        lista_nome_stats.append('zoom Multiplier')

        runSpeedMultiplierads=adsStats['runSpeedMultiplier']*6.75    #aim stats
        lista_stats.append(runSpeedMultiplierads)
        lista_nome_stats.append('run Speed Multiplier ads')

        firstBulletAccuracyads=adsStats['firstBulletAccuracy']
        lista_stats.append(firstBulletAccuracyads)
        lista_nome_stats.append('first Bullet Accuracy ads')

    except:
        pass

    rangeEndMeters=damageranges[0]['rangeEndMeters']
    lista_stats.append(rangeEndMeters)
    lista_nome_stats.append('range End Meters')

    headDamage=damageranges[0]['headDamage']
    lista_stats.append(headDamage)
    lista_nome_stats.append('head Damage')

    bodyDamage=damageranges[0]['bodyDamage']               #near stats
    lista_stats.append(bodyDamage)
    lista_nome_stats.append('body Damage')

    legDamage=damageranges[0]['legDamage']
    lista_stats.append(legDamage)
    lista_nome_stats.append('leg Damage')

    try:
        rangeEndMetersfar=damageranges[1]['rangeEndMeters']
        lista_stats.append(rangeEndMetersfar)
        lista_nome_stats.append('range End Meters far')

        headDamagefar=damageranges[1]['headDamage']
        lista_stats.append(headDamagefar)
        lista_nome_stats.append('head Damage far')

        bodyDamagefar=damageranges[1]['bodyDamage']            # far stats
        lista_stats.append(bodyDamagefar)
        lista_nome_stats.append('body Damage far')

        legDamagefar=damageranges[1]['legDamage']
        lista_stats.append(legDamagefar)
        lista_nome_stats.append('leg Damage far')

        rangefar=True

    except:
        rangefar=False

    
    return lista_stats,lista_nome_stats,rangefar

