from stacking_params import *


thresh = lim_sim.halos.M > mass_cut

map_zs = (lim_sim.mapinst.nu_rest/lim_sim.mapinst.nu_bincents) - 1

halo_zs = lim_sim.halos.redshift[thresh]
good_halo_zs = np.where(np.logical_and(halo_zs >= map_zs[ind] - err, halo_zs <= map_zs[ind] + err))

halo_xs = lim_sim.halos.ra[thresh][good_halo_zs]
halo_ys = lim_sim.halos.dec[thresh][good_halo_zs]
halo_zs = halo_zs[good_halo_zs]

print('The total forecast observing time has been set to', t_obs, '.')

pure_map, noisy_map = lum(lim_sim, n, halo_xs, halo_ys, halo_zs)

pure_stack, noisy_stack = np.nanmean(pure_map, axis = 0), np.nanmean(noisy_map, axis = 0)


fig , axes = plt.subplots(nrows = 2, ncols = 1, figsize = (8, 15))

plt.subplot(211)
plt.imshow(pure_stack, cmap = 'CMRmap', extent = [-0.65, 0.65, -0.65, 0.65])
plt.title(r'$Pure\ Signal\ Stacked\ Map$', math_fontfamily = 'dejavuserif')
plt.xlabel(r'$RA$', math_fontfamily='dejavuserif')
plt.ylabel(r'$DEC$', math_fontfamily='dejavuserif')
cb1 = plt.colorbar(label = r'$Jy/sr$')
ax1 = cb1.ax
text1 = ax1.yaxis.label
font = matplotlib.font_manager.FontProperties(math_fontfamily='dejavuserif', style='italic', size=16)
text1.set_font_properties(font)


plt.subplot(212)
plt.imshow(noisy_stack, cmap = 'CMRmap', extent = [-0.65, 0.65, -0.65, 0.65])
plt.title(r'$Forecast\ Stacked\ Map$', math_fontfamily = 'dejavuserif')
plt.xlabel(r'$RA$', math_fontfamily='dejavuserif')
plt.ylabel(r'$DEC$', math_fontfamily='dejavuserif')
cb2 = plt.colorbar(label = r'$Jy/sr$')
ax2 = cb2.ax
text2 = ax2.yaxis.label
font = matplotlib.font_manager.FontProperties(math_fontfamily='dejavuserif', style='italic', size=16)
text2.set_font_properties(font)

plt.savefig('Stacking/stacking_simv2.png', bbox_inches = "tight")
plt.show()

